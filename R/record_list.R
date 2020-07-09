{
  print("What are your three favorite things in life?")
  a <- c()
  for(i in 1:3){
    new <- readline(prompt = paste("\t", i,") ", sep=""))
    a <- c(a,new)
  }
  for(item in a){
    print(item)
  }
  
}
