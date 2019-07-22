import configparser

if __name__ == '__main__':
    
    config = configparser.ConfigParser()
    
    config.add_section("接口测试")

    config.set("接口测试","班级","31期")
    config.set("接口测试","口号","好好学习")
    config.set("接口测试","外号","天天向上")

    with open('iniConfig.ini','w') as configfile:
        config.write(configfile)