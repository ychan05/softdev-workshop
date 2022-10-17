  Luigi (he/they):: Yat Long Chan, Brian Wang
  SoftDev pd 8
  K12: Form(s) Take and Give
  2022-10-17
  time spent: 0.5 hours

Predictions:
1. dspl_page
  1. prints app that code is running on (Atom), what the code is asking for, and arguments
     given in code to terminal
  2. runs the code under the login.html template

2. authenticate
  1. prints app that code is running on, what the code is asking for, and arguments
     given in code to terminal
  2. returns a website with "Waaaa hooo HAAAH"

Results:
1. dspl_page (we were wrong)
  1. prints the app running the code (Flask), the place where the code is ran (server),
     and the dictionary of the arguments given in webpage
  2. runs the code under the login.html template

2. authenticate (we were wrong)
  1. prints the app running the code (Flask), the place where the code is ran (server),
     and the dictionary of the arguments given in webpage
  2. transitions the website into one that says "Waaaa hooo HAAAH"

DISCO:
- A HTTP 405 error is thrown when GET is excluded from method field in app.route()
- the args dictionary is updated with user inputs
- special chars are stored in forms dict w/ '\' 
- the request method isn't needed to load and use webpage in browser, but stores user inputs.
- When the methods are included in app.route(), we cannot access the values stored in request.args


QCC:
- What are GET and POST requests?
- How are do they differ?
