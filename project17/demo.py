import requests
import json


BASE_URl = 'http://127.0.0.1:8000/'
END_POINT = 'api/'


def create_resource():
	name = input('Enter the Student Name :\t')
	email = input('Enter the Student email :\t')
	phone_num = input('Enter the Student phone number :\t')
	address = input('Enter the Student address :\t')
	student_data = {'name': name, 'email': email, 'phone_num': phone_num, 'address': address}
	response = requests.post(BASE_URl + END_POINT, data = json.dumps(student_data) )
	print(response.status_code)
	print(response.json())


def select_complete_resource(id = None):
	data = {}
	if id is not None:
		data  = {'id': id}
	response = requests.get(BASE_URl + END_POINT, data = json.dumps(data))
	print(response.status_code)
	print(response.json())

def select_single_resource():
	id = input('Enter the id to select record :\t')
	data = {}
	if id is not None:
		data = {'id': id}
	response = requests.get(BASE_URl + END_POINT , data = json.dumps(data))
	print(response.status_code)
	print(response.json())


def update_partially():
	id = input('Enter the id to record data partially:\t')
	update_data = { 'id': id, 'name': 'rani', 'address': 'mumbai'}
	response = requests.put(BASE_URl + END_POINT , data = json.dumps(update_data))
	print(response.status_code)
	print(response.json())

def update_completely():
	id = input('Enter the id to update record :\t')
	name = input('Enter the Student Name :\t')
	email = input('Enter the Student email :\t')
	phone_num = input('Enter the Student phone number :\t')
	address = input('Enter the Student address :\t')	

	update_data = { 'id': id, 'name': name, 'email': email, 'phone_num': phone_no, 'address': address}
	response = requests.put(BASE_URl + END_POINT , data = json.dumps(update_data))
	print(response.status_code)
	print(response.json())

def delete_resource():
	id = input('Enter the id to delete record :\t')
	data = {'id': id}
	response = requests.delete(BASE_URl + END_POINT, data = json.dumps(data))
	print(response.status_code)
	print(response.json())
	

def invalidOption():
	print('please provide valid option')
	

if __name__ == '__main__':

	while(1):
		print(''' 
			Please Select the below operation.
			1. Create the data.2. Select single resource.
			3. Select complete resource.4. Update partially.
			5. Update Completely.6. Delete the resource.
			
			 ''')

		choice = int(input('Enter your choice:'))

		options = {
			1: create_resource,2: select_single_resource,
			3: select_complete_resource,4: update_partially,
			5: update_completely,6: delete_resource,
			
		}
		options.get(choice, invalidOption)()


