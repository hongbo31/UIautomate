import xml.etree.cElementTree as ET


class ReadConfig:

    def __init__(self):
        xml_file_path = 'C:\\Users\\monitor\\PycharmProjects\\UIAuto\\testFile\\config.xml'
        self.tree = ET.parse(xml_file_path)
        self.root = self.tree.getroot()

    # def xml_pathType(self):
    #     for path_type in self.root.iter('name'):
    #         return (path_type.text)
    def get_element_method(self):
        list = []
        for children in self.root.findall('element'):
            name = children.find('name').text
            path_type = children.find('pathType').text
            path_value = children.find('pathValue').text
            t = [name, path_type, path_value]
            list.append(t)
        return list

    def getPathType(self, name):
        list = ReadConfig().get_element_method()
        for i in list:
            if i[0] == name:
                return i[1]

    def getPathValue(self, name):
        list = ReadConfig().get_element_method()
        for i in list:
            if i[0] == name:
                return i[2]


if __name__ == '__main__':
    r1 = ReadConfig()
    print(r1.get_element_method())
    print(r1.getPathType('email'))
    print(r1.getPathValue('email'))
