import requests


class Divar:
    def __init__(self, city):

        self.city = city


        """
        :param city: pass wanted city name, list of valid cities are bellow
        """
        self.cities = ['mashhad', 'karaj', 'shiraz', 'isfahan', 'ahvaz', 'tabriz', 'kermanshah', 'qom', 'rasht',
                       'abadan', 'abadeh', 'abdanan', 'abyek', 'azarshahr', 'astara', 'astaneh-ashrafiyeh', 'ashkhaneh',
                       'aq-qala', 'amol', 'abhar', 'arak', 'ardabil', 'ardakan', 'urmia', 'azna', 'asadabad',
                       'esfarāyen', 'eslamabad-gharb', 'eslamshahr', 'oshnavieh', 'alvand', 'aligudarz', 'andimeshk',
                       'ahar', 'izeh', 'iranshahr', 'ilam', 'eyvan', 'babol', 'babolsar', 'baneh', 'bojnurd',
                       'borazjan', 'borujerd', 'boroujen', 'bam', 'bonab', 'bandar-imam-khomeini', 'bandar-anzali',
                       'bandar-torkaman', 'bandar-abbas', 'bandar-kangan', 'bandar-ganaveh', 'bandar-mahshahr',
                       'bushehr', 'bukan', 'behbahan', 'behshahr', 'bijar', 'birjand', 'parsabad', 'piranshahr',
                       'pishva', 'takestan', 'talesh', 'torbat-jam', 'tonekabon', 'tuyserkan', 'tehran', 'javanrud',
                       'juybar', 'jahrom', 'jiroft', 'chaboksar', 'chabahar', 'chalus', 'chahar-dangeh', 'hamidia',
                       'khorramabad', 'khorramdarreh', 'khorramshahr', 'khalkhal', 'khomein', 'khoy', 'darab',
                       'damghan', 'dezful', 'damavand', 'dorud', 'dogonbadan', 'dehdasht', 'dehloran', 'ramsar',
                       'ramhormoz', 'rafsanjan', 'rudsar', 'zabol', 'zahedan', 'zarand', 'zanjan', 'sari', 'saveh',
                       'sabzevar', 'sarab', 'saravan', 'sarpol-zahab', 'sardasht', 'saqqez', 'salmas', 'semnan',
                       'sonqor', 'sanandaj', 'susangerd', 'sahand', 'siahkal', 'sirjan', 'shahroud', 'shahin-dej',
                       'shush', 'shooshtar', 'sadra', 'shahrekord', 'shirvan', 'someh-sara', 'taleqan', 'tabas',
                       'aliabad-katul', 'farrokhshahr', 'ferdows', 'fereydunkenar', 'falavarjan', 'fuman', 'qaemshahr',
                       'ghayen', 'qorveh', 'qazvin', 'qeshm', 'qeydar', 'kashan', 'kordkuy', 'kerman', 'kelachay',
                       'kangavar', 'kuhdasht', 'kish', 'gorgan', 'garmsar', 'golpayegan', 'gomishan', 'gonabad',
                       'gonbad-kavus', 'lahijan', 'lordegan', 'langarud', 'masal', 'maku', 'mahalat', 'mohammadiyeh',
                       'mahmudabad', 'maragheh', 'marand', 'marivan', 'masjed-soleyman', 'meshgin-shahr', 'malayer',
                       'mahabad', 'miandoab', 'mianeh', 'meybod', 'minab', 'najafabad', 'nasimshahr', 'nazarabad',
                       'naqadeh', 'neka', 'nur', 'nurabad', 'nowshahr', 'nahavand', 'neyshabur', 'hamedan', 'yasuj',
                       'yazd']

        if self.city not in self.cities:
            raise ValueError
