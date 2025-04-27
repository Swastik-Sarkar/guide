struct player{
  var name = "Iso"
  var age = 19
  var nationality = "Valorant"
}

let playerInstance = player()
var name = playerInstance.name
var age = playerInstance.age
var nationality = playerInstance.nationality
if age > 18{
  print("\(name) is at legal age to vote!")
} else if age < 18{
    print("\(name) is not at legal age to vote!")
} 
