from cmd import Cmd





class Term(Cmd):
    banner ="""

            ___________            .___              ___________.__                            _____             .____    .__  _____       
            \_   _____/ _____    __| _/____   ____   \_   _____/|__|__  __ ____               /  |  |            |    |   |__|/ ____\____  
            |    __)_ /     \  / __ |/ __ \_/ __ \   |    __)  |  \  \/ // __ \    ______   /   |  |_   ______  |    |   |  \   __\/ __ \ 
            |        \  Y Y  \/ /_/ \  ___/\  ___/   |     \   |  |\   /\  ___/   /_____/  /    ^   /  /_____/  |    |___|  ||  | \  ___/ 
            /_______  /__|_|  /\____ |\___  >\___  >  \___  /   |__| \_/  \___  >           \____   |            |_______ \__||__|  \___  >
                    \/      \/      \/    \/     \/       \/                  \/                 |__|                    \/             \/ 

            """
    prompt = '(md5) '
    



class Ctl_del(Exception):
    pass


if __name__ =='__main__':

    try:
        Term().cmdloop(intro=Term.banner)
    except:
        if KeyboardInterrupt:
            print("[*]...Exiting")