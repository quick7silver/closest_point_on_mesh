import math
mesh_vertex = [[0.14877812564373016, -0.9876883625984192, -0.048340942710638046],
[0.12655822932720184, -0.9876883625984192, -0.0919499322772026],
[0.0919499322772026, -0.9876883625984192, -0.12655822932720184],
[0.04834093526005745, -0.9876883625984192, -0.14877811074256897],
[0.0, -0.9876883625984192, -0.1564345508813858],
[-0.04834093526005745, -0.9876883625984192, -0.14877809584140778],
[-0.09194991737604141, -0.9876883625984192, -0.12655819952487946],
[-0.12655818462371826, -0.9876883625984192, -0.09194990247488022],
[-0.1487780660390854, -0.9876883625984192, -0.048340924084186554],
[-0.15643452107906342, -0.9876883625984192, 0.0],
[-0.1487780660390854, -0.9876883625984192, 0.048340924084186554],
[-0.12655818462371826, -0.9876883625984192, 0.09194989502429962],
[-0.09194989502429962, -0.9876883625984192, 0.12655816972255707],
[-0.048340924084186554, -0.9876883625984192, 0.1487780511379242],
[-4.662110697495336e-09, -0.9876883625984192, 0.15643449127674103],
[0.04834090918302536, -0.9876883625984192, 0.148778036236763],
[0.09194988012313843, -0.9876883625984192, 0.12655815482139587],
[0.12655815482139587, -0.9876883625984192, 0.09194988757371902],
[0.148778036236763, -0.9876883625984192, 0.04834091290831566],
[0.15643447637557983, -0.9876883625984192, 0.0],
[0.29389283061027527, -0.9510565400123596, -0.09549156576395035],
[0.2500001788139343, -0.9510565400123596, -0.18163573741912842],
[0.18163573741912842, -0.9510565400123596, -0.25000014901161194],
[0.09549155086278915, -0.9510565400123596, -0.2938928008079529],
[0.0, -0.9510565400123596, -0.309017151594162],
[-0.09549155086278915, -0.9510565400123596, -0.2938927710056305],
[-0.18163570761680603, -0.9510565400123596, -0.25000008940696716],
[-0.25000008940696716, -0.9510565400123596, -0.18163569271564484],
[-0.2938927114009857, -0.9510565400123596, -0.09549152851104736],
[-0.3090170621871948, -0.9510565400123596, 0.0],
[-0.2938927114009857, -0.9510565400123596, 0.09549152851104736],
[-0.2500000596046448, -0.9510565400123596, 0.18163567781448364],
[-0.18163567781448364, -0.9510565400123596, 0.2500000596046448],
[-0.09549152851104736, -0.9510565400123596, 0.29389268159866333],
[-9.209424334244432e-09, -0.9510565400123596, 0.30901703238487244],
[0.09549149870872498, -0.9510565400123596, 0.29389265179634094],
[0.18163563311100006, -0.9510565400123596, 0.2500000298023224],
[0.25, -0.9510565400123596, 0.18163564801216125],
[0.29389265179634094, -0.9510565400123596, 0.09549150615930557],
[0.30901700258255005, -0.9510565400123596, 0.0],
[0.431770920753479, -0.8910065293312073, -0.14029087126255035],
[0.3672862946987152, -0.8910065293312073, -0.2668491005897522],
[0.2668491005897522, -0.8910065293312073, -0.3672862648963928],
[0.14029085636138916, -0.8910065293312073, -0.43177086114883423],
[0.0, -0.8910065293312073, -0.45399072766304016],
[-0.14029085636138916, -0.8910065293312073, -0.43177083134651184],
[-0.2668490409851074, -0.8910065293312073, -0.36728617548942566],
[-0.36728614568710327, -0.8910065293312073, -0.26684901118278503],
[-0.43177077174186707, -0.8910065293312073, -0.14029081165790558],
[-0.453990638256073, -0.8910065293312073, 0.0],
[-0.43177077174186707, -0.8910065293312073, 0.14029081165790558],
[-0.3672861158847809, -0.8910065293312073, 0.26684898138046265],
[-0.26684898138046265, -0.8910065293312073, 0.3672861158847809],
[-0.14029081165790558, -0.8910065293312073, 0.4317707121372223],
[-1.352997180958937e-08, -0.8910065293312073, 0.4539905786514282],
[0.1402907818555832, -0.8910065293312073, 0.4317706823348999],
[0.26684892177581787, -0.8910065293312073, 0.3672860860824585],
[0.3672860562801361, -0.8910065293312073, 0.26684895157814026],
[0.4317706525325775, -0.8910065293312073, 0.14029079675674438],
[0.45399051904678345, -0.8910065293312073, 0.0],
[0.5590173602104187, -0.80901700258255, -0.18163573741912842],
[0.4755285680294037, -0.80901700258255, -0.3454917073249817],
[0.3454917073249817, -0.80901700258255, -0.4755285382270813],
[0.18163572251796722, -0.80901700258255, -0.5590173006057739],
[0.0, -0.80901700258255, -0.587785542011261],
[-0.18163572251796722, -0.80901700258255, -0.5590172410011292],
[-0.3454916477203369, -0.80901700258255, -0.47552841901779175],
[-0.47552838921546936, -0.80901700258255, -0.34549158811569214],
[-0.5590171217918396, -0.80901700258255, -0.18163566291332245],
[-0.5877853631973267, -0.80901700258255, 0.0],
[-0.5590171217918396, -0.80901700258255, 0.18163566291332245],
[-0.475528359413147, -0.80901700258255, 0.34549155831336975],
[-0.34549155831336975, -0.80901700258255, 0.4755283296108246],
[-0.18163566291332245, -0.80901700258255, 0.5590170621871948],
[-1.751736533606163e-08, -0.80901700258255, 0.5877853035926819],
[0.18163561820983887, -0.80901700258255, 0.5590170621871948],
[0.345491498708725, -0.80901700258255, 0.4755282998085022],
[0.4755282700061798, -0.80901700258255, 0.34549152851104736],
[0.55901700258255, -0.80901700258255, 0.18163563311100006],
[0.5877852439880371, -0.80901700258255, 0.0],
[0.6724989414215088, -0.7071067690849304, -0.21850813925266266],
[0.5720617771148682, -0.7071067690849304, -0.4156271815299988],
[0.4156271815299988, -0.7071067690849304, -0.5720617175102234],
[0.21850812435150146, -0.7071067690849304, -0.672498881816864],
[0.0, -0.7071067690849304, -0.7071071267127991],
[-0.21850812435150146, -0.7071067690849304, -0.6724988222122192],
[-0.4156270921230316, -0.7071067690849304, -0.5720615983009338],
[-0.5720615386962891, -0.7071067690849304, -0.41562706232070923],
[-0.6724987030029297, -0.7071067690849304, -0.2185080498456955],
[-0.7071069478988647, -0.7071067690849304, 0.0],
[-0.6724987030029297, -0.7071067690849304, 0.2185080498456955],
[-0.5720615386962891, -0.7071067690849304, 0.41562700271606445],
[-0.41562700271606445, -0.7071067690849304, 0.5720614790916443],
[-0.2185080498456955, -0.7071067690849304, 0.6724985837936401],
[-2.107342389479072e-08, -0.7071067690849304, 0.7071068286895752],
[0.21850799024105072, -0.7071067690849304, 0.6724985837936401],
[0.4156269133090973, -0.7071067690849304, 0.5720614194869995],
[0.5720614194869995, -0.7071067690849304, 0.41562697291374207],
[0.6724985241889954, -0.7071067690849304, 0.2185080200433731],
[0.7071067690849304, -0.7071067690849304, 0.0],
[0.769421398639679, -0.5877852439880371, -0.25000014901161194],
[0.6545089483261108, -0.5877852439880371, -0.4755285382270813],
[0.4755285382270813, -0.5877852439880371, -0.6545088887214661],
[0.25000011920928955, -0.5877852439880371, -0.7694212794303894],
[0.0, -0.5877852439880371, -0.8090173602104187],
[-0.25000011920928955, -0.5877852439880371, -0.7694212198257446],
[-0.47552844882011414, -0.5877852439880371, -0.6545087695121765],
[-0.6545087099075317, -0.5877852439880371, -0.47552838921546936],
[-0.7694211006164551, -0.5877852439880371, -0.2500000596046448],
[-0.8090171813964844, -0.5877852439880371, 0.0],
[-0.7694211006164551, -0.5877852439880371, 0.2500000596046448],
[-0.654508650302887, -0.5877852439880371, 0.475528359413147],
[-0.475528359413147, -0.5877852439880371, 0.6545085906982422],
[-0.2500000596046448, -0.5877852439880371, 0.7694209814071655],
[-2.4110585528092088e-08, -0.5877852439880371, 0.8090171217918396],
[0.2499999850988388, -0.5877852439880371, 0.7694209814071655],
[0.4755282700061798, -0.5877852439880371, 0.6545085310935974],
[0.6545085310935974, -0.5877852439880371, 0.4755282998085022],
[0.7694209218025208, -0.5877852439880371, 0.25],
[0.80901700258255, -0.5877852439880371, 0.0],
[0.8473981022834778, -0.45399051904678345, -0.2753363251686096],
[0.7208399176597595, -0.45399051904678345, -0.5237208008766174],
[0.5237208008766174, -0.45399051904678345, -0.7208398580551147],
[0.27533629536628723, -0.45399051904678345, -0.8473979830741882],
[0.0, -0.45399051904678345, -0.8910069465637207],
[-0.27533629536628723, -0.45399051904678345, -0.8473979830741882],
[-0.5237206816673279, -0.45399051904678345, -0.7208396792411804],
[-0.7208396196365356, -0.45399051904678345, -0.5237206220626831],
[-0.8473978042602539, -0.45399051904678345, -0.27533620595932007],
[-0.8910067677497864, -0.45399051904678345, 0.0],
[-0.8473978042602539, -0.45399051904678345, 0.27533620595932007],
[-0.7208396196365356, -0.45399051904678345, 0.5237206220626831],
[-0.5237206220626831, -0.45399051904678345, 0.7208395600318909],
[-0.27533620595932007, -0.45399051904678345, 0.8473976850509644],
[-2.655406383667014e-08, -0.45399051904678345, 0.8910066485404968],
[0.2753361463546753, -0.45399051904678345, 0.8473976254463196],
[0.5237205028533936, -0.45399051904678345, 0.7208395004272461],
[0.7208394408226013, -0.45399051904678345, 0.5237205624580383],
[0.8473975658416748, -0.45399051904678345, 0.2753361761569977],
[0.8910065293312073, -0.45399051904678345, 0.0],
[0.9045091271400452, -0.30901697278022766, -0.2938928008079529],
[0.769421398639679, -0.30901697278022766, -0.5590173602104187],
[0.5590173602104187, -0.30901697278022766, -0.7694213390350342],
[0.2938927710056305, -0.30901697278022766, -0.9045090079307556],
[0.0, -0.30901697278022766, -0.9510570168495178],
[-0.2938927710056305, -0.30901697278022766, -0.9045089483261108],
[-0.5590172410011292, -0.30901697278022766, -0.7694212198257446],
[-0.7694211602210999, -0.30901697278022766, -0.5590171813964844],
[-0.9045087695121765, -0.30901697278022766, -0.2938927114009857],
[-0.9510567784309387, -0.30901697278022766, 0.0],
[-0.9045087695121765, -0.30901697278022766, 0.2938927114009857],
[-0.7694211006164551, -0.30901697278022766, 0.5590171217918396],
[-0.5590171217918396, -0.30901697278022766, 0.7694210410118103],
[-0.2938927114009857, -0.30901697278022766, 0.904508650302887],
[-2.8343693614374388e-08, -0.30901697278022766, 0.9510566592216492],
[0.29389262199401855, -0.30901697278022766, 0.9045085906982422],
[0.55901700258255, -0.30901697278022766, 0.7694209814071655],
[0.7694209218025208, -0.30901697278022766, 0.5590170621871948],
[0.9045085310935974, -0.30901697278022766, 0.29389265179634094],
[0.9510565400123596, -0.30901697278022766, 0.0],
[0.939348042011261, -0.15643437206745148, -0.30521267652511597],
[0.7990571856498718, -0.15643437206745148, -0.5805490016937256],
[0.5805490016937256, -0.15643437206745148, -0.799057126045227],
[0.3052126467227936, -0.15643437206745148, -0.9393479228019714],
[0.0, -0.15643437206745148, -0.9876888394355774],
[-0.3052126467227936, -0.15643437206745148, -0.9393478631973267],
[-0.580548882484436, -0.15643437206745148, -0.7990569472312927],
[-0.799056887626648, -0.15643437206745148, -0.5805488228797913],
[-0.9393476843833923, -0.15643437206745148, -0.3052125573158264],
[-0.9876886010169983, -0.15643437206745148, 0.0],
[-0.9393476843833923, -0.15643437206745148, 0.3052125573158264],
[-0.7990568280220032, -0.15643437206745148, 0.5805487632751465],
[-0.5805487632751465, -0.15643437206745148, 0.7990567684173584],
[-0.3052125573158264, -0.15643437206745148, 0.9393475651741028],
[-2.9435407000732994e-08, -0.15643437206745148, 0.9876884818077087],
[0.30521246790885925, -0.15643437206745148, 0.9393475651741028],
[0.5805486440658569, -0.15643437206745148, 0.7990567088127136],
[0.7990566492080688, -0.15643437206745148, 0.5805487036705017],
[0.939347505569458, -0.15643437206745148, 0.30521249771118164],
[0.9876883625984192, -0.15643437206745148, 0.0],
[0.9510571360588074, 0.0, -0.3090171813964844],
[0.809017539024353, 0.0, -0.5877856016159058],
[0.5877856016159058, 0.0, -0.8090174794197083],
[0.309017151594162, 0.0, -0.9510570168495178],
[0.0, 0.0, -1.0000004768371582],
[-0.309017151594162, 0.0, -0.951056957244873],
[-0.5877854824066162, 0.0, -0.8090173006057739],
[-0.8090172410011292, 0.0, -0.5877854228019714],
[-0.9510567784309387, 0.0, -0.3090170621871948],
[-1.000000238418579, 0.0, 0.0],
[-0.9510567784309387, 0.0, 0.3090170621871948],
[-0.8090171813964844, 0.0, 0.5877853631973267],
[-0.5877853631973267, 0.0, 0.8090171217918396],
[-0.3090170621871948, 0.0, 0.9510566592216492],
[-2.9802322387695312e-08, 0.0, 1.0000001192092896],
[0.30901697278022766, 0.0, 0.9510565996170044],
[0.5877852439880371, 0.0, 0.8090170621871948],
[0.80901700258255, 0.0, 0.5877853035926819],
[0.9510565400123596, 0.0, 0.30901700258255005],
[1.0, 0.0, 0.0],
[0.939348042011261, 0.15643437206745148, -0.30521267652511597],
[0.7990571856498718, 0.15643437206745148, -0.5805490016937256],
[0.5805490016937256, 0.15643437206745148, -0.799057126045227],
[0.3052126467227936, 0.15643437206745148, -0.9393479228019714],
[0.0, 0.15643437206745148, -0.9876888394355774],
[-0.3052126467227936, 0.15643437206745148, -0.9393478631973267],
[-0.580548882484436, 0.15643437206745148, -0.7990569472312927],
[-0.799056887626648, 0.15643437206745148, -0.5805488228797913],
[-0.9393476843833923, 0.15643437206745148, -0.3052125573158264],
[-0.9876886010169983, 0.15643437206745148, 0.0],
[-0.9393476843833923, 0.15643437206745148, 0.3052125573158264],
[-0.7990568280220032, 0.15643437206745148, 0.5805487632751465],
[-0.5805487632751465, 0.15643437206745148, 0.7990567684173584],
[-0.3052125573158264, 0.15643437206745148, 0.9393475651741028],
[-2.9435407000732994e-08, 0.15643437206745148, 0.9876884818077087],
[0.30521246790885925, 0.15643437206745148, 0.9393475651741028],
[0.5805486440658569, 0.15643437206745148, 0.7990567088127136],
[0.7990566492080688, 0.15643437206745148, 0.5805487036705017],
[0.939347505569458, 0.15643437206745148, 0.30521249771118164],
[0.9876883625984192, 0.15643437206745148, 0.0],
[0.9045091271400452, 0.30901697278022766, -0.2938928008079529],
[0.769421398639679, 0.30901697278022766, -0.5590173602104187],
[0.5590173602104187, 0.30901697278022766, -0.7694213390350342],
[0.2938927710056305, 0.30901697278022766, -0.9045090079307556],
[0.0, 0.30901697278022766, -0.9510570168495178],
[-0.2938927710056305, 0.30901697278022766, -0.9045089483261108],
[-0.5590172410011292, 0.30901697278022766, -0.7694212198257446],
[-0.7694211602210999, 0.30901697278022766, -0.5590171813964844],
[-0.9045087695121765, 0.30901697278022766, -0.2938927114009857],
[-0.9510567784309387, 0.30901697278022766, 0.0],
[-0.9045087695121765, 0.30901697278022766, 0.2938927114009857],
[-0.7694211006164551, 0.30901697278022766, 0.5590171217918396],
[-0.5590171217918396, 0.30901697278022766, 0.7694210410118103],
[-0.2938927114009857, 0.30901697278022766, 0.904508650302887],
[-2.8343693614374388e-08, 0.30901697278022766, 0.9510566592216492],
[0.29389262199401855, 0.30901697278022766, 0.9045085906982422],
[0.55901700258255, 0.30901697278022766, 0.7694209814071655],
[0.7694209218025208, 0.30901697278022766, 0.5590170621871948],
[0.9045085310935974, 0.30901697278022766, 0.29389265179634094],
[0.9510565400123596, 0.30901697278022766, 0.0],
[0.8473981022834778, 0.45399051904678345, -0.2753363251686096],
[0.7208399176597595, 0.45399051904678345, -0.5237208008766174],
[0.5237208008766174, 0.45399051904678345, -0.7208398580551147],
[0.27533629536628723, 0.45399051904678345, -0.8473979830741882],
[0.0, 0.45399051904678345, -0.8910069465637207],
[-0.27533629536628723, 0.45399051904678345, -0.8473979830741882],
[-0.5237206816673279, 0.45399051904678345, -0.7208396792411804],
[-0.7208396196365356, 0.45399051904678345, -0.5237206220626831],
[-0.8473978042602539, 0.45399051904678345, -0.27533620595932007],
[-0.8910067677497864, 0.45399051904678345, 0.0],
[-0.8473978042602539, 0.45399051904678345, 0.27533620595932007],
[-0.7208396196365356, 0.45399051904678345, 0.5237206220626831],
[-0.5237206220626831, 0.45399051904678345, 0.7208395600318909],
[-0.27533620595932007, 0.45399051904678345, 0.8473976850509644],
[-2.655406383667014e-08, 0.45399051904678345, 0.8910066485404968],
[0.2753361463546753, 0.45399051904678345, 0.8473976254463196],
[0.5237205028533936, 0.45399051904678345, 0.7208395004272461],
[0.7208394408226013, 0.45399051904678345, 0.5237205624580383],
[0.8473975658416748, 0.45399051904678345, 0.2753361761569977],
[0.8910065293312073, 0.45399051904678345, 0.0],
[0.769421398639679, 0.5877852439880371, -0.25000014901161194],
[0.6545089483261108, 0.5877852439880371, -0.4755285382270813],
[0.4755285382270813, 0.5877852439880371, -0.6545088887214661],
[0.25000011920928955, 0.5877852439880371, -0.7694212794303894],
[0.0, 0.5877852439880371, -0.8090173602104187],
[-0.25000011920928955, 0.5877852439880371, -0.7694212198257446],
[-0.47552844882011414, 0.5877852439880371, -0.6545087695121765],
[-0.6545087099075317, 0.5877852439880371, -0.47552838921546936],
[-0.7694211006164551, 0.5877852439880371, -0.2500000596046448],
[-0.8090171813964844, 0.5877852439880371, 0.0],
[-0.7694211006164551, 0.5877852439880371, 0.2500000596046448],
[-0.654508650302887, 0.5877852439880371, 0.475528359413147],
[-0.475528359413147, 0.5877852439880371, 0.6545085906982422],
[-0.2500000596046448, 0.5877852439880371, 0.7694209814071655],
[-2.4110585528092088e-08, 0.5877852439880371, 0.8090171217918396],
[0.2499999850988388, 0.5877852439880371, 0.7694209814071655],
[0.4755282700061798, 0.5877852439880371, 0.6545085310935974],
[0.6545085310935974, 0.5877852439880371, 0.4755282998085022],
[0.7694209218025208, 0.5877852439880371, 0.25],
[0.80901700258255, 0.5877852439880371, 0.0],
[0.6724989414215088, 0.7071067690849304, -0.21850813925266266],
[0.5720617771148682, 0.7071067690849304, -0.4156271815299988],
[0.4156271815299988, 0.7071067690849304, -0.5720617175102234],
[0.21850812435150146, 0.7071067690849304, -0.672498881816864],
[0.0, 0.7071067690849304, -0.7071071267127991],
[-0.21850812435150146, 0.7071067690849304, -0.6724988222122192],
[-0.4156270921230316, 0.7071067690849304, -0.5720615983009338],
[-0.5720615386962891, 0.7071067690849304, -0.41562706232070923],
[-0.6724987030029297, 0.7071067690849304, -0.2185080498456955],
[-0.7071069478988647, 0.7071067690849304, 0.0],
[-0.6724987030029297, 0.7071067690849304, 0.2185080498456955],
[-0.5720615386962891, 0.7071067690849304, 0.41562700271606445],
[-0.41562700271606445, 0.7071067690849304, 0.5720614790916443],
[-0.2185080498456955, 0.7071067690849304, 0.6724985837936401],
[-2.107342389479072e-08, 0.7071067690849304, 0.7071068286895752],
[0.21850799024105072, 0.7071067690849304, 0.6724985837936401],
[0.4156269133090973, 0.7071067690849304, 0.5720614194869995],
[0.5720614194869995, 0.7071067690849304, 0.41562697291374207],
[0.6724985241889954, 0.7071067690849304, 0.2185080200433731],
[0.7071067690849304, 0.7071067690849304, 0.0],
[0.5590173602104187, 0.80901700258255, -0.18163573741912842],
[0.4755285680294037, 0.80901700258255, -0.3454917073249817],
[0.3454917073249817, 0.80901700258255, -0.4755285382270813],
[0.18163572251796722, 0.80901700258255, -0.5590173006057739],
[0.0, 0.80901700258255, -0.587785542011261],
[-0.18163572251796722, 0.80901700258255, -0.5590172410011292],
[-0.3454916477203369, 0.80901700258255, -0.47552841901779175],
[-0.47552838921546936, 0.80901700258255, -0.34549158811569214],
[-0.5590171217918396, 0.80901700258255, -0.18163566291332245],
[-0.5877853631973267, 0.80901700258255, 0.0],
[-0.5590171217918396, 0.80901700258255, 0.18163566291332245],
[-0.475528359413147, 0.80901700258255, 0.34549155831336975],
[-0.34549155831336975, 0.80901700258255, 0.4755283296108246],
[-0.18163566291332245, 0.80901700258255, 0.5590170621871948],
[-1.751736533606163e-08, 0.80901700258255, 0.5877853035926819],
[0.18163561820983887, 0.80901700258255, 0.5590170621871948],
[0.345491498708725, 0.80901700258255, 0.4755282998085022],
[0.4755282700061798, 0.80901700258255, 0.34549152851104736],
[0.55901700258255, 0.80901700258255, 0.18163563311100006],
[0.5877852439880371, 0.80901700258255, 0.0],
[0.431770920753479, 0.8910065293312073, -0.14029087126255035],
[0.3672862946987152, 0.8910065293312073, -0.2668491005897522],
[0.2668491005897522, 0.8910065293312073, -0.3672862648963928],
[0.14029085636138916, 0.8910065293312073, -0.43177086114883423],
[0.0, 0.8910065293312073, -0.45399072766304016],
[-0.14029085636138916, 0.8910065293312073, -0.43177083134651184],
[-0.2668490409851074, 0.8910065293312073, -0.36728617548942566],
[-0.36728614568710327, 0.8910065293312073, -0.26684901118278503],
[-0.43177077174186707, 0.8910065293312073, -0.14029081165790558],
[-0.453990638256073, 0.8910065293312073, 0.0],
[-0.43177077174186707, 0.8910065293312073, 0.14029081165790558],
[-0.3672861158847809, 0.8910065293312073, 0.26684898138046265],
[-0.26684898138046265, 0.8910065293312073, 0.3672861158847809],
[-0.14029081165790558, 0.8910065293312073, 0.4317707121372223],
[-1.352997180958937e-08, 0.8910065293312073, 0.4539905786514282],
[0.1402907818555832, 0.8910065293312073, 0.4317706823348999],
[0.26684892177581787, 0.8910065293312073, 0.3672860860824585],
[0.3672860562801361, 0.8910065293312073, 0.26684895157814026],
[0.4317706525325775, 0.8910065293312073, 0.14029079675674438],
[0.45399051904678345, 0.8910065293312073, 0.0],
[0.29389283061027527, 0.9510565400123596, -0.09549156576395035],
[0.2500001788139343, 0.9510565400123596, -0.18163573741912842],
[0.18163573741912842, 0.9510565400123596, -0.25000014901161194],
[0.09549155086278915, 0.9510565400123596, -0.2938928008079529],
[0.0, 0.9510565400123596, -0.309017151594162],
[-0.09549155086278915, 0.9510565400123596, -0.2938927710056305],
[-0.18163570761680603, 0.9510565400123596, -0.25000008940696716],
[-0.25000008940696716, 0.9510565400123596, -0.18163569271564484],
[-0.2938927114009857, 0.9510565400123596, -0.09549152851104736],
[-0.3090170621871948, 0.9510565400123596, 0.0],
[-0.2938927114009857, 0.9510565400123596, 0.09549152851104736],
[-0.2500000596046448, 0.9510565400123596, 0.18163567781448364],
[-0.18163567781448364, 0.9510565400123596, 0.2500000596046448],
[-0.09549152851104736, 0.9510565400123596, 0.29389268159866333],
[-9.209424334244432e-09, 0.9510565400123596, 0.30901703238487244],
[0.09549149870872498, 0.9510565400123596, 0.29389265179634094],
[0.18163563311100006, 0.9510565400123596, 0.2500000298023224],
[0.25, 0.9510565400123596, 0.18163564801216125],
[0.29389265179634094, 0.9510565400123596, 0.09549150615930557],
[0.30901700258255005, 0.9510565400123596, 0.0],
[0.14877812564373016, 0.9876883625984192, -0.048340942710638046],
[0.12655822932720184, 0.9876883625984192, -0.0919499322772026],
[0.0919499322772026, 0.9876883625984192, -0.12655822932720184],
[0.04834093526005745, 0.9876883625984192, -0.14877811074256897],
[0.0, 0.9876883625984192, -0.1564345508813858],
[-0.04834093526005745, 0.9876883625984192, -0.14877809584140778],
[-0.09194991737604141, 0.9876883625984192, -0.12655819952487946],
[-0.12655818462371826, 0.9876883625984192, -0.09194990247488022],
[-0.1487780660390854, 0.9876883625984192, -0.048340924084186554],
[-0.15643452107906342, 0.9876883625984192, 0.0],
[-0.1487780660390854, 0.9876883625984192, 0.048340924084186554],
[-0.12655818462371826, 0.9876883625984192, 0.09194989502429962],
[-0.09194989502429962, 0.9876883625984192, 0.12655816972255707],
[-0.048340924084186554, 0.9876883625984192, 0.1487780511379242],
[-4.662110697495336e-09, 0.9876883625984192, 0.15643449127674103],
[0.04834090918302536, 0.9876883625984192, 0.148778036236763],
[0.09194988012313843, 0.9876883625984192, 0.12655815482139587],
[0.12655815482139587, 0.9876883625984192, 0.09194988757371902],
[0.148778036236763, 0.9876883625984192, 0.04834091290831566],
[0.15643447637557983, 0.9876883625984192, 0.0],
[0.0, -1.0, 0.0],
[0.0, 1.0, 0.0],]

random_point = [1.2, 1.3, 1.5]
max_distance = 1.6


class ValidPoint (object):
    def __init__(self, coordinates, distance):
        self.coord = coordinates
        self.dist = distance

def closest_vertex(mesh_vertex, random_point, max_distance):
    valid_points = []
    for mesh_point in mesh_vertex:
        distance = math.sqrt(math.pow((mesh_point[0]-random_point[0]),2)+math.pow((mesh_point[1]-random_point[1]),2)+math.pow((mesh_point[2]-random_point[2]),2))
        if distance <= max_distance:
            valid_points.append(ValidPoint(mesh_point, distance))
    valid_points.sort(key= lambda x: x.dist)
    return valid_points[0].coord

if __name__ == "__main__":
    closest_point = closest_vertex(mesh_vertex, random_point, max_distance)
    print closest_point