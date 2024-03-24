from my_class import port_http, port_ssh, port_sql, port_ftp
import json

class ports_map():

    def __init__(self):
        self.http=None
        self.ssh=None
        self.sql=None
        self.ftp=None
        #self.scan_all(ip)

    def scan(self,ip,protocol):
        if protocol=="http":
            self.scan_http(ip)
        elif protocol=='ssh':
            self.scan_ssh(ip)
        elif protocol=='sql':
            self.scan_sql(ip)
        elif protocol=='ftp':
            self.scan_ftp(ip)
    
    def scan_http(self,ip):
        self.http=port_http.port_http()
        self.http.test_port2(ip)
        #print(self.http.to_dict())


    def scan_ssh(self,ip):
        self.ssh=port_ssh.port_ssh()
        self.ssh.test_port2(ip)
        #self.ssh.to_dict()

    def scan_sql(self,ip):
        self.sql=port_sql.port_sql()
        self.sql.test_port2(ip)
    
    def scan_ftp(self,ip):
        self.ftp=port_ftp.port_ftp()
        self.ftp.test_port2(ip)

    def to_dict(self):
        return {
            'http_port': self.http.to_dict() if self.http else self.http,
            'ssh_port':self.ssh.to_dict() if self.ssh else self.ssh,
            'sql_port': self.sql.to_dict() if self.sql else self.sql,
            'ftp_port': self.ftp.to_dict() if self.ftp else self.ftp
        }
    def to_json(self):
        return json.dumps(self.to_dict())
    
