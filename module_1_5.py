my_container=1,'проба',True
print(my_container)
my_container[1]='замена'
print(my_container)

#Кортеж хранит только ссылки на объекты, но не сами объекты. Поэтому он не может контролировать изменение объектов, ссылки на которые он хранит, он может гарантировать только то, что набор ссылок внутри него не будет изменен.

my_list=[1,'проба',True]
print(my_list)
my_list[1]='замена'
print(my_list)