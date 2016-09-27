from os.path import dirname
from traceback import format_exc
from time import time
this_dir = dirname(__file__)

try:
    from reclaimer.halo.meta.handler import MapLoader

    path   = "D:\\Program Files\\Microsoft Games\\Halo Custom Edition\\maps\\"
    loader = MapLoader(debug=1, allow_corrupt=True)
    
    input('Press Enter to begin loading resource maps in:\n'+
          '    %s\n\n' % path)
    
    start = time()
    
    sounds  = loader.build_tag(filepath=path+'sounds.map',  def_id="resource")
    #bitmaps = loader.build_tag(filepath=path+'bitmaps.map', def_id="resource")
    #strings = loader.build_tag(filepath=path+'loc.map',     def_id="resource")
    #halomap = loader.build_tag(filepath=path+'Smoke Screen\\CE_bloodgulch.map', def_id="map")

    sounds.pprint(printout=True, show=['name','value','subtrees','index','type'])
    #bitmaps.pprint(printout=True, show=['name','value','subtrees','index','type'])
    #strings.pprint(printout=True, show=['name','value','subtrees','index','type'])
    #halomap.pprint(printout=True, show=['name','value','subtrees','index','type'])
    
    input('-'*80 + '\n'+
          'Finished.\n'+
          'Operation took %s seconds.\n'%(time()-start) +
          '\n'+
          'Press enter to exit.')

except:
    print(format_exc())
    input()