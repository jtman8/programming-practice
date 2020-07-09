
a <- function() {
  li = c()
  for(i in 1:100000){
    li = c(li,i)
  }
  return(li)
}
start <- Sys.time()
a()
print(Sys.time() - start)
