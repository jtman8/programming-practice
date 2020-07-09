library(stringr)
{
  words <- readline(prompt="Give me a word, any word: ")
  while(!grepl("^[A-Za-z]+$", words, perl=T)){
    words <- readline(prompt="I said a word! Try again. Give me a word, any word: ")
  } 
  print(paste("Hey! ",str_to_title(words)," is a cool word!", sep=""))
}
