#------------------------------------------
# Sudoku Solver to Practice R
# Anna Hickerson 6/8/2015
#------------------------------------------

# Create a data frame that contains all
# possible values for all positions in sudoku
#------------------------------------------

# r_pos - row position
# c_pos - column position
# s_pos - square position
# p_val - possible value
  

r_pos <- rep(1:9, each = 9)
c_pos <- rep(1:9, 9)
s_pos <- rep(rep(1:3, each=3), 3)
s_pos <- c(s_pos, rep(rep(4:6, each=3), 3))
s_pos <- c(s_pos, rep(rep(7:9, each=3), 3))


puzzle <- data.frame(r_pos = r_pos, c_pos = c_pos, s_pos = s_pos,
                     val1 = TRUE, val2 = TRUE, val3 = TRUE,
                     val4 = TRUE, val5 = TRUE, val6 = TRUE,
                     val7 = TRUE, val8 = TRUE, val9 = TRUE)

# series of functions to help manipulate the puzzle data
#------------------------------------------

# function to set possible values into puzzle
set_value <- function(i, j, p_val) {
  puzzle[puzzle$r_pos == i & puzzle$c_pos == j, 4:12] <<- p_val
}

# function to get possible values into puzzle
get_value <- function(i, j) {
  p_val <- puzzle[puzzle$r_pos == i & puzzle$c_pos == j, 4:12]
  p_val <- as.logical(p_val)
  p_val
}

# function to generate a logical p_val vector
p_val_func <- function(true_vals) {
  p_val <- rep(FALSE, 9)
  for(i in true_vals) {
    p_val[i] <- TRUE
    
  }
  p_val
}

# function to set (i.e. initialize) all values of specific puzzle
set_puzzle <- function(init_puzzle) {
  for(i in 1:9) {
    for(j in 1:9) {
      if(!is.na(init_puzzle[i,j])) {
        set_value(i,j, p_val_func(init_puzzle[i,j]))
      }
    }
  }
}

# function to get and display all values of specific puzzle as matrix
get_puzzle <- function() {
  display_puzzle <- matrix(rep(NA,81), nrow=9, ncol=9)
  for(i in 1:9) {
    for(j in 1:9) {
      p_val <- get_value(i,j)
      if(sum(p_val)==1) {
        # determine what the value is
        value <- 1:9
        value <- value[p_val]
        # set the value into the display puzzle
        display_puzzle[i,j] <- value
      }
    }
  }
  print(display_puzzle)
}


# set values to specific puzzle
#------------------------------------------
init_puzzle <- matrix(c(1, 2, 4, 3, 9, 6, 5, NA, NA,
                          7, NA, NA, NA, NA, NA, 3, 9, 2,
                          NA, 9, NA, NA, NA, NA, NA, 4, NA,
                          NA, NA, NA, 4, 3, 9, 2, NA, NA,
                          NA, 7, NA, NA, NA, NA, NA, 5, NA,
                          NA, NA, 2, 6, 5, 7, NA, NA, NA,
                          NA, 4, NA, NA, NA, NA, NA, 6, NA,
                          2, 6, 7, NA, NA, NA, NA, NA, 9,
                          NA, NA, 8, 1, 6, 3, 7, 2, 4), nrow=9, ncol=9)
init_puzzle <- t(init_puzzle)

set_puzzle(init_puzzle)

get_puzzle()

# Solve the puzzle
#------------------------------------------
for(iterations in 1:10) {
  for(i in 1:9) {
    for(j in 1:9) {
      # if the value for the specific location is solved
      current_p_val <- get_value(i,j)
      
      if(sum(current_p_val)==1) {
        # determine what the value is
        value <- 1:9
        value <- value[current_p_val]
        
        # set all others of that value in the same row as false
        puzzle[puzzle$r_pos==i & puzzle$c_pos != j,value+3] <- FALSE
        
        # set all others of that value in the same column as false
        puzzle[puzzle$r_pos!=i & puzzle$c_pos == j,value+3] <- FALSE
        
        # set all others of that value in the same square as false
        s_pos <- puzzle$s_pos[puzzle$r_pos==i & puzzle$c_pos == j]
        puzzle[!(puzzle$r_pos==i & puzzle$c_pos == j) &  puzzle$s_pos == s_pos,value+3] <- FALSE
        
      }
    }
  }
  print(iterations)
  if(!any(is.na(get_puzzle()))) break
}
