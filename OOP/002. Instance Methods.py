class Mohamed(object):
    def callMe(self):
        print("calling 'callMe' method with instance: ")
        print(self)
    greeting = "Hello Mohamed"

thisMohamed = Mohamed()
print(Mohamed.greeting)
thisMohamed.callMe()
print(thisMohamed)