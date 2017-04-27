from supyr_struct.field_type_methods import *
from .constants import *


def tag_ref_sizecalc(self, node, **kwargs):
    '''
    Used to calculate the size of a tag reference string from a given string
    '''
    node = node.split(self.str_delimiter)[0]
    if node:
        return len(node) + 1
    return 0

def tag_ref_size(node=None, parent=None, attr_index=None,
                 rawdata=None, new_value=None, **kwargs):
    '''Used to retrieve or set the byte size of a Halo tag
    reference string. If the string is empty, the actual amount
    of bytes it takes up is zero, otherwise it is (1+length) bytes.
    This is to account for the delimiter.
    
    When setting the size, the provided new_value is expected to
    be including the delimiter, so the reverse operation is applied.
    If the string's length is 1(only a delimiter), the bytes size
    is zero, but otherwise it is (length-1).

    Lengths of 1 cant exist.'''
    
    if new_value is None:
        strlen = parent.path_length
        strlen += 1*bool(strlen)
        return strlen
    if new_value <= 1:
        parent.path_length = 0
    else:
        parent.path_length = new_value - 1


def encode_tag_ref_str(self, node, parent=None, attr_index=None):
    """This function is the same as encode_string, except that
    when a halo reference string has zero length, the string doesnt
    actually exist. It's not just a delimiter character, the string
    isn't stored at all. To make it work, we instead return an
    empty bytes object if the string length is zero"""
    if node:
        return encode_string(self, node, parent=parent, attr_index=attr_index)
    return b''


def reflexive_parser(self, desc, node=None, parent=None, attr_index=None,
                     rawdata=None, root_offset=0, offset=0, **kwargs):
    """
    """
    try:
        __lsi__ = list.__setitem__
        orig_offset = offset
        if node is None:
            parent[attr_index] = node = desc.get(BLOCK_CLS, self.node_cls)\
                (desc, parent=parent)

        # If there is rawdata to build the structure from
        if rawdata is not None:
            offsets = desc['ATTR_OFFS']
            struct_off = root_offset + offset

            if self.f_endian == '=':
                for i in range(len(node)):
                    off = struct_off + offsets[i]
                    typ = desc[i]['TYPE']
                    __lsi__(node, i,
                            unpack(typ.enc, rawdata[off:off + typ.size])[0])
            elif self.f_endian == '<':
                for i in range(len(node)):
                    off = struct_off + offsets[i]
                    typ = desc[i]['TYPE']
                    __lsi__(node, i, unpack(typ.little.enc,
                                            rawdata[off:off + typ.size])[0])
            else:
                for i in range(len(node)):
                    off = struct_off + offsets[i]
                    typ = desc[i]['TYPE']
                    __lsi__(node, i, unpack(typ.big.enc,
                                            rawdata[off:off + typ.size])[0])

            # increment offset by the size of the struct
            offset += desc['SIZE']
        else:
            for i in range(len(node)):
                __lsi__(node, i,
                        desc[i].get(DEFAULT, desc[i]['TYPE'].default()))

        s_desc = desc.get('STEPTREE')
        if s_desc:
            if 'magic' in kwargs:
                offset = node[1] - kwargs["magic"]
            if 'steptree_parents' not in kwargs:
                offset = s_desc['TYPE'].parser(s_desc, None, node, 'STEPTREE',
                                               rawdata, root_offset, offset,
                                               **kwargs)
            else:
                kwargs['steptree_parents'].append(node)

        # pass the incremented offset to the caller
        return offset
    except Exception as e:
        # if the error occurred while parsing something that doesnt have an
        # error report routine built into the function, do it for it.
        kwargs.update(buffer=rawdata, root_offset=root_offset)
        if 's_desc' in locals():
            e = format_parse_error(e, field_type=s_desc.get(TYPE), desc=s_desc,
                                  parent=node, attr_index=STEPTREE,
                                  offset=offset, **kwargs)
        elif 'i' in locals():
            e = format_parse_error(e, field_type=desc[i].get(TYPE),
                                   desc=desc[i], parent=node, attr_index=i,
                                   offset=offset, **kwargs)
        e = format_parse_error(e, field_type=self, desc=desc,
                               parent=parent, attr_index=attr_index,
                               offset=orig_offset, **kwargs)
        raise e


def rawdata_parser(self, desc, node=None, parent=None, attr_index=None,
                   rawdata=None, root_offset=0, offset=0, **kwargs):
    if rawdata is not None:
        bytecount = parent.size

        if 'magic' in kwargs:
            offset = parent.pointer - kwargs['magic']
            if offset < 0 or offset + bytecount > len(rawdata):
                offset = parent.raw_pointer
        rawdata.seek(root_offset + offset)
        parent[attr_index] = self.node_cls(rawdata.read(bytecount))
        return offset + bytecount

    parent[attr_index] = self.node_cls(b'\x00'*parent.size)
    return offset
