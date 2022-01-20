class Hash:
    def set(self,array_data,key,value):
        index = 0
        exist_flag = 0
        for count in array_data:
            if(count[0] == key):
                exist_flag = 1
                array_data[index] = (key,value)
            index = index + 1
        if(exist_flag == 0):
            array_data.append((key,value))
        return array_data
    def get(self,array_data,key):
        for count in array_data:
            if(count[0] == key):
                return count[1]


#usage
system_info = []
hash_obj = Hash()
system_info = hash_obj.set(system_info,'name2','sibin')
system_info = hash_obj.set(system_info,'age2','25')
print(hash_obj.get(system_info,'name2'))
print(system_info)
