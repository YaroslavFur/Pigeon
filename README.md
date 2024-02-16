# Pigeon
Pigeon (P-Gen) (Password Generator) - custom passwords storing app.
Python app for windows & android that hashes the single secret phrase with servicename & username provided by the user to generate unique and different passwords for every site/service/user. Services & usernames are stored in memory for quick selection. Pigeon user only needs to know & input one secret phrase to get any password needed. It's basically custom passwords storing app.

> Uses Kivy framework.
> Hashing is being done using single simple SHA-256, so to protect the secret phrase (it's basically the key to all your accounts everywhere) from potential dictionary attacks it is **highly** recommended to use randomized & long secret phrase.
> 
> The custom app only I am gonna use, not professional or planned to be distributed in any way. Code/project free to everyone though.
> Advantages:
> - No more remembering passwords (except the only secret phrase)
> - No relying on the third part (except the app itself)
> - Randomized, good & different passwords for any site
> Disadvantages:
> - Need to use the app every time you need to enter the password in any your service/site
> - Need (not necesseraly though) to save servicenames, usernames, password lengths etc in a separate storage, no cloud save or cross device communication, app's totally offline, it's just a hasher
> - One key to all your life
