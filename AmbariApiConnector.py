'''
Created by JaKu
Version : 0.10
'''
import requests
from urllib3 import disable_warnings
from requests import get, post, put, delete
from json import loads


class AmbariApiConnector:
    def __init__(
            self,
            protocol,
            domain,
            port,
            user,
            user_passwd,
            cluster_name,
            verbose=0,
            ):
        self.__protocol = protocol
        self.__domain = domain
        self.__port = port
        self.__user = user
        self.__user_passwd = user_passwd
        self.cluster_name = cluster_name
        self.verbose = verbose
        self.url = ''.join([
            self.__protocol,
            "://",
            self.__domain,
            ":",
            self.__port,
            ])
        self.headers = {
            "X-Requested-By" : "ambari",
            }

    def get(self, api_string):
        request = get(
            self.url + api_string,
            auth=(self.__user, self.__user_passwd),
            verify=False,
            headers=self.headers,
            )
        if self.verbose:
            print "GET: OK!\n"
        return loads(request.text)

    def post(self, api_string, post_content):
        request = post(
            self.url + api_string,
            data=post_content,
            auth=(self.__user, self.__user_passwd),
            verify=False,
            headers=self.headers,
            )
        if self.verbose:
            if request.text:
                print request.text
            else:
                print "POST: OK!"

    def put(self, api_string, post_content):
        request = put(
            self.url + api_string,
            data=post_content,
            auth=(self.__user, self.__user_passwd),
            verify=False,
            headers=self.headers,
            )
        if self.verbose:
            if request.text:
                print request.text
            else:
                print "PUT: OK!"

    def delete(self, api_string):
        request = delete(
            self.url + api_string,
            auth=(self.__user, self.__user_passwd),
            verify=False,
            headers=self.headers,
            )
        if self.verbose:
            if request.text:
                print request.text
            else:
                print "DELETE: OK!"

    disable_warnings()

def main():
    ac = AmbariApiConnector('https', 'ambari.domain.net', '9999', 'user', 'passwd', 'cluster_name')
    
    # GET #
    print(ac.get("/api/v1/clusters/"+ ac.cluster_name +"/privileges"))
    
    # POST #
    #post_string = "[{\"PrivilegeInfo\" : {\"permission_name\" : \"SERVICE.ADMINISTRATOR\",\"principal_name\" : \"AD_GROUP_NAME\",\"principal_type\" : \"GROUP\"}}]"
    #ac.post("/api/v1/clusters/"+ ac.cluster_name +"/privileges", post_string)

    # PUT #
    #put_string = "[{\"PrivilegeInfo\" : {\"permission_name\" : \"SERVICE.ADMINISTRATOR\",\"principal_name\" : \"AD_GROUP_NAME\",\"principal_type\" : \"GROUP\"}}]"
    #ac.put("/api/v1/clusters/"+ ac.cluster_name +"/privileges", put_string)

    # DELETE #
    #ac.delete("/api/v1/clusters/"+ac.cluster_name+"/privileges/1000000")
    
if __name__=="__main__":
    main()