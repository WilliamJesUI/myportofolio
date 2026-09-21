Name : William Jesiel

NPM : 2506637155

Class : PBP KKI

### Assignment 1
1. I used the "section" element as I am adding a new section onto my website which is the personal project section. I feel it helped make my html code more organized as it is now separated from my "about me" section.
2. At first I experienced difficulties in trying to center the images. I also struggled on how to make them horizontally aligned with each other. When it comes to determining which elements need to be repositioned or resized, I just mainly choose whatever looks good and neat in my eyes.
3. I'd feel like I definitely wanted to add more pages and fun interactive things for the user to do! More pages would definitely help me organize my portfolio. With interactivity it would be cool if I could fill my homepage with animations.

"DID not use AI" 
I mainly studied from the W3school website! I found their premade templates really helpful. My work process mainly revolves around using their generic template and reformatting it so it looks nice on my page. I also refer to some sections from tutorial 1, especially with the flexbox styling. I change somethings a little mainly through trial and error until I get the desired look!


### Assignment 2
1. From the user point of view, they would notice only the new 'achievement' page. In reality, I actually refactored the main page by changing the originally hardcoded project flipcards into for loops. Although it makes zero difference for the viewers, it makes a huge difference for me as the developer due to reasons I will explain in number 2. Also Idk why in the PWS I have to retype the shell code to insert my projects and experience. Its so frustrating everytime I push to PWS all my projects, experience and achievement is gone. >:(
2. For me, I think storing the data in the model actually made my html file way shorter since I can now iterate through all the data with a for loop. As a result, this made my code more readable. Not only that, I can now easily modify which data I want to display. Example using If and else, I could show perhaps the projects that has 'burhan' in it. If it were to be hard coded I would have to manually select which projects to remove and it will give me a headache.
3. The 'makemigrations' command will create some python files that will either create or modify the database. Inside the python file lies the instruction that tell the database what needs to be done. Then after 'makemigrations' there is the 'migrate'. 'migrate' will actually apply the changes to the database, updating its schema accordingly.

"DID not use AI"

I still have not used AI in the making of this assignment. I felt like this part is more straightforward because I've watched a free lecture from CS50W Harvard in youtube that discusses about the MVT. The explanation was amazing and I was able to immediately implement it by referring to their notes online. Of course I also found the tutorial 2 helpful, I followed the steps there to create my new models 'Project' and 'Achievement'. Unit tests weren't that bad aswell because I previously learned it in DDP2. 

Low-key I don't know how much longer I can survive without AI. I want to make my website beautiful but it seems so impossible without AI because I don't have much time :( CSS is so hard.

### Assignment 3
1. Creating HTML forms manually can be extremely tedious and time-consuming. It will also take longer time to refactor or edit the forms. So instead we use Django's ModelForm which is much more convenient. A csrf token increases safety as it makes sure the forms sent is actually from you the user and not an external malicious party.
2. JSON is easier to use than XML. It is also highly compatible with javascript a language that is very common in modern web applications.
3. So the user would send in a request. urls.py sees the path matches "api/achievements/" and routes the request to get_achievements_json. The function in views will then fetch the data from database which is then serialized meaning it is converted from python objects to JSON. Then the JSON is finally sent back to the user/client.

AI disclosure
I asked AI (Claude) for help in the creation of the update feature because I was stuck and had no idea how to implement it. I mainly asked for the general idea by prompting "How might I implement an update button beside the delete button. What steps should I take." Then claude generate the steps and some boilerplate which I then used as reference in helping me create the update feature. I also used claude to help with debugging the search bar which I also struggled to implement. 