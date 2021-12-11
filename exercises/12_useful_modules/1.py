import subprocess
def ping_ip_addresses():
	with open("ip's.txt", "r") as ip_s:
		ips = ip_s.readlines()
		while True:
			result = []
			for ip in ips:
				p = subprocess.Popen(["ping", ip])
				result.append(p)
			try_again = []
			for ip, p, in zip(ips,result):
				if p.wait() == 0:
					print(ip, "it's ok")
				else:
					print(ip, "failed")
					try_again.append(ip)
				print(try_again)
ping_ip_addresses()
