import pdb 
from models.task import Task
from models.user import User

import repositories.task_repository as task_repository
import repositories.user_repository as user_repository 

user_repository.delete_all()
task_repository.delete_all()

user_1 = User("Jack", "Jarvis")
user_repository.save(user_1)

user_2 = User("Victor", "McDade")
user_repository.save(user_2)

task_1 = Task("Walk Dog", user_1, 60)
task_repository.save(task_1)

task_2 = Task("Feed Cat", user_2, 5)
task_repository.save(task_2)

# task_1.mark_complete()
# task_repository.update(task_1)
# user_respository.select_all()


