# update()
'''
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]
'''
	# Update dict1 from a dict2/collection_of_2-tuples
dictionary = {"One":1, "Zero":False, False:0, "Initial-list":[0, 1], (0, 1):"Initial-tuple", "Proposition":{True:1, False:0}, 3.2:"3.2", "F":False}
list_of_two_tuples = [('x', 1), ('y', 2), ('z', 3)]
test_dict = {"One":"This is a one", "Zero":"This is a zero", "Two":"This is a two"}
zipObj = zip("This", range(10, 20))
print("The dictionary is %r" % dictionary)
print("Updating the dictionary from the list of 2-tuples %r" % list_of_two_tuples)
dictionary.update(list_of_two_tuples)
print("The dictionary now is %r" % dictionary)
print("Updating the dictionary from the dictionary %r" % test_dict)
dictionary.update(test_dict)
print("The dictionary now is %r" % dictionary)
print("Updating the dictionary from the zip object %r" % zipObj)
dictionary.update(zipObj)
print("The dictionary now is %r" % dictionary)

