import requests, sys
from bs4 import BeautifulSoup
#source language
source_language = [
    "US",
    "CA",
    "AF",
    "AL",
    "DZ",
    "AS",
    "AD",
    "AO",
    "AI",
    "AQ",
    "AG",
    "AR",
    "AM",
    "AW",
    "AU",
    "AT",
    "AZ",
    "BS",
    "BH",
    "BD",
    "BB",
    "BY",
    "BE",
    "BZ",
    "BJ",
    "BM",
    "BT",
    "BO",
    "BA",
    "BW",
    "BV",
    "BR",
    "IO",
    "BN",
    "BG",
    "BF",
    "BI",
    "KH",
    "CM",
    "CV",
    "KY",
    "CF",
    "TD",
    "CL",
    "CN",
    "CX",
    "CC",
    "CO",
    "KM",
    "CG",
    "CD",
    "CK",
    "CR",
    "HR",
    "CU",
    "CY",
    "CZ",
    "DK",
    "DJ",
    "DM",
    "DO",
    "TP",
    "EC",
    "EG",
    "SV",
    "GQ",
    "ER",
    "EE",
    "ET",
    "FK",
    "FO",
    "FJ",
    "FI",
    "FR",
    "FX",
    "GF",
    "TF",
    "GA",
    "GM",
    "GE",
    "DE",
    "GH",
    "GI",
    "GR",
    "GL",
    "GD",
    "GP",
    "GU",
    "GT",
    "GN",
    "GW",
    "GY",
    "HT",
    "HM",
    "VA",
    "HN",
    "HK",
    "HU",
    "IS",
    "IN",
    "ID",
    "IR",
    "IQ",
    "IE",
    "IL",
    "IT",
    "CI",
    "JM",
    "JP",
    "JO",
    "KZ",
    "KE",
    "KI",
    "KW",
    "KG",
    "LA",
    "LV",
    "LB",
    "LS",
    "LR",
    "LY",
    "LI",
    "LT",
    "LU",
    "MO",
    "MK",
    "MG",
    "MW",
    "MY",
    "MV",
    "ML",
    "MT",
    "MH",
    "MQ",
    "MR",
    "MU",
    "YT",
    "MX",
    "FM",
    "MD",
    "MC",
    "MN",
    "MS",
    "MA",
    "MZ",
    "MM",
    "NA",
    "NR",
    "NP",
    "NL",
    "AN",
    "NC",
    "NZ",
    "NI",
    "NE",
    "NG",
    "NU",
    "NF",
    "KP",
    "MP",
    "NO",
    "OM",
    "PK",
    "PW",
    "PS",
    "PA",
    "PG",
    "PY",
    "PE",
    "PH",
    "PN",
    "PL",
    "PF",
    "PT",
    "PR",
    "QA",
    "RE",
    "RO",
    "RU",
    "RW",
    "GS",
    "SH",
    "KN",
    "LC",
    "PM",
    "VC",
    "WS",
    "SM",
    "ST",
    "SA",
    "SN",
    "SC",
    "SL",
    "SG",
    "SK",
    "SI",
    "SB",
    "SO",
    "ZA",
    "KR",
    "ES",
    "LK",
    "SD",
    "SR",
    "SZ",
    "SE",
    "CH",
    "SY",
    "TW",
    "TJ",
    "TZ",
    "TH",
    "TG",
    "TK",
    "TO",
    "TT",
    "TN",
    "TR",
    "TM",
    "TC",
    "TV",
    "UG",
    "UA",
    "AE",
    "GB",
    "UY",
    "UM",
    "UZ",
    "VU",
    "VE",
    "VN",
    "VG",
    "VI",
    "WF",
    "EH",
    "YE",
    "YU",
    "ZR",
    "ZM",
    "ZW"
]
#target language
target_language = [
    "US",
    "CA",
    "AF",
    "AL",
    "DZ",
    "AS",
    "AD",
    "AO",
    "AI",
    "AQ",
    "AG",
    "AR",
    "AM",
    "AW",
    "AU",
    "AT",
    "AZ",
    "BS",
    "BH",
    "BD",
    "BB",
    "BY",
    "BE",
    "BZ",
    "BJ",
    "BM",
    "BT",
    "BO",
    "BA",
    "BW",
    "BV",
    "BR",
    "IO",
    "BN",
    "BG",
    "BF",
    "BI",
    "KH",
    "CM",
    "CV",
    "KY",
    "CF",
    "TD",
    "CL",
    "CN",
    "CX",
    "CC",
    "CO",
    "KM",
    "CG",
    "CD",
    "CK",
    "CR",
    "HR",
    "CU",
    "CY",
    "CZ",
    "DK",
    "DJ",
    "DM",
    "DO",
    "TP",
    "EC",
    "EG",
    "SV",
    "GQ",
    "ER",
    "EE",
    "ET",
    "FK",
    "FO",
    "FJ",
    "FI",
    "FR",
    "FX",
    "GF",
    "TF",
    "GA",
    "GM",
    "GE",
    "DE",
    "GH",
    "GI",
    "GR",
    "GL",
    "GD",
    "GP",
    "GU",
    "GT",
    "GN",
    "GW",
    "GY",
    "HT",
    "HM",
    "VA",
    "HN",
    "HK",
    "HU",
    "IS",
    "IN",
    "ID",
    "IR",
    "IQ",
    "IE",
    "IL",
    "IT",
    "CI",
    "JM",
    "JP",
    "JO",
    "KZ",
    "KE",
    "KI",
    "KW",
    "KG",
    "LA",
    "LV",
    "LB",
    "LS",
    "LR",
    "LY",
    "LI",
    "LT",
    "LU",
    "MO",
    "MK",
    "MG",
    "MW",
    "MY",
    "MV",
    "ML",
    "MT",
    "MH",
    "MQ",
    "MR",
    "MU",
    "YT",
    "MX",
    "FM",
    "MD",
    "MC",
    "MN",
    "MS",
    "MA",
    "MZ",
    "MM",
    "NA",
    "NR",
    "NP",
    "NL",
    "AN",
    "NC",
    "NZ",
    "NI",
    "NE",
    "NG",
    "NU",
    "NF",
    "KP",
    "MP",
    "NO",
    "OM",
    "PK",
    "PW",
    "PS",
    "PA",
    "PG",
    "PY",
    "PE",
    "PH",
    "PN",
    "PL",
    "PF",
    "PT",
    "PR",
    "QA",
    "RE",
    "RO",
    "RU",
    "RW",
    "GS",
    "SH",
    "KN",
    "LC",
    "PM",
    "VC",
    "WS",
    "SM",
    "ST",
    "SA",
    "SN",
    "SC",
    "SL",
    "SG",
    "SK",
    "SI",
    "SB",
    "SO",
    "ZA",
    "KR",
    "ES",
    "LK",
    "SD",
    "SR",
    "SZ",
    "SE",
    "CH",
    "SY",
    "TW",
    "TJ",
    "TZ",
    "TH",
    "TG",
    "TK",
    "TO",
    "TT",
    "TN",
    "TR",
    "TM",
    "TC",
    "TV",
    "UG",
    "UA",
    "AE",
    "GB",
    "UY",
    "UM",
    "UZ",
    "VU",
    "VE",
    "VN",
    "VG",
    "VI",
    "WF",
    "EH",
    "YE",
    "YU",
    "ZR",
    "ZM",
    "ZW"
]
def banner():
	print """
	\x1b[1;34mG \x1b[1;31mO \x1b[1;33mO \x1b[1;34mG \x1b[1;32mL \x1b[1;31mE\x1b[0m TRANSLATE
	"""
def help():
	print '\x1b[1;31m[!]\x1b[0m Usage : python2 gtranslate.py [SL-TL] "text to translate!"'
	print '    Example : gtranslate.py US-ID "nice to meet you"\n'
	
class GoogleTranslate:
	def __init__(self):
		self.url = 'https://translate.google.com/'
		
	#set translation
	def set_translation(self, sl_to_tl):
		self.translation = sl_to_tl.split('-')
		try:
			self.sl = self.translation[0]
			self.tl = self.translation[1]
		except IndexError:
			banner()
			help()
			sys.exit(1)
			
		#check if sl and tl available in list of source language and target language
		if self.sl in source_language and self.tl in target_language:
			self.url = self.url + 'm?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=' % (source_language[source_language.index(self.sl)], target_language[target_language.index(self.tl)])
		else:
			banner()
			help()
			sys.exit(1)
			
	#translate
	def get_translated(self, text):
		try:
			self.req = requests.get(self.url+text)
			self.soup = BeautifulSoup(self.req.content, 'html.parser')
			self.content = self.soup.find_all(class_ = 't0')
			self.result = [result.text for result in self.content]
			return self.result
			
		except requests.HTTPError as e:
			print '\x1b[1;31m[!]\x1b[0m Error : %s' % e
			sys.exit(1)
		except requests.RequestException as e:
			print '\x1b[1;31m[!]\x1b[0m Error : %s' % e
			sys.exit(1)
		except requests.ConnectionError as e:
			print '\x1b[1;31m[!]\x1b[0m Error : %s' % e
			sys.exit(1)
		except requests.Timeout as e:
			print '\x1b[1;31m[!]\x1b[0m Error : %s' % e
			sys.exit(1)
			
if __name__ == '__main__':
	translate = GoogleTranslate()
	if len(sys.argv) == 3:
		banner()
		translate.set_translation(sys.argv[1])
		for translated in translate.get_translated(str(sys.argv[2])):
			print '\x1b[1;32m[+]\x1b[0m %s\n' % translated
	else:
		banner()
		help()
		sys.exit(1)
