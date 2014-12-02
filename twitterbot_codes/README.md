Medical Joke Bot (Twitter)

This code will search a Mongo Database for health related terms and make jokes related to the health terms as replies to the users.

All required files in twitterbot_codes:

joke_generator.py handles the joke creation definitions
regex_generator.py has all the code for dealing with the Mongo Database (searching, etc)
latest_mongo_id.txt stores the latest mongo ID used in the search to create effecient searching
symptoms.txt and synonyms.txt can be edited to modify what sort of tweets are found.
twitterbot.py has the main working code of the bot.

All that needs to be done is to add authentication details for your twitterbot to the oauth definition within twitterbot.py