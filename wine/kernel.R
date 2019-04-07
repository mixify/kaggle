#1번
red_data <- read.csv("winequality-red.csv", sep=";")
red_data
white_data <- read.csv("winequality-white.csv", sep=";")
white_data

red_data[!complete.cases(red_data),]#결측치 없음
white_data[!complete.cases(white_data),]#결측치 없음

opar <- par(mfrow = c(2,2))
plot(quality ~., data=red_data)
plot(quality ~., data=white_data)

#2번
library(mlbench) 
m_red <- lm(quality ~ ., data=red_data)
m_white <- lm(quality ~ ., data=white_data)

m_red_both <- step(m_red, direction="both")
null = lm(quality~1, data=red_data)
full = lm(quality~., data=red_data)
m_red_forward <- step(null, direction="forward",scope = list(lower=NULL, upper=full))
m_red_backward <- step(m_red, direction="backward")

m_white_both <- step(m_white, direction="both")
null = lm(quality~1, data=white_data)
full = lm(quality~., data=white_data)
m_white_forward <- step(null, direction="forward",scope = list(lower=NULL, upper=full))
m_white_backward <- step(m_white, direction="backward")

#3번
cor(red_data[,1:11])
symnum(cor(red_data[,1:11]))

#4번
opar = par(mfrow=c(1,1))
plot(m_red_both)

plot(m_white_both)

red_inter <- lm(quality ~ (fixed.acidity+volatile.acidity+citric.acid+residual.sugar+chlorides+free.sulfur.dioxide+total.sulfur.dioxide+density+pH+sulphates+alcohol)^2, data=red_data)
red_inter
summary(m_red)
summary(red_inter)

white_inter <- lm(quality ~ (fixed.acidity+volatile.acidity+citric.acid+residual.sugar+chlorides+free.sulfur.dioxide+total.sulfur.dioxide+density+pH+sulphates+alcohol)^2, data=white_data)
white_inter
summary(m_white)
summary(white_inter)


#5번
library(car)
outlierTest(m_red_both)
m_rm_out_red <- lm(formula(m_red_both), data=red_data[-833,])

outlierTest(m_white_both)
m_rm_out_white <- lm(formula(m_white_both), data=white_data[-c(4746,2782,3308,254,446),])

summary(m_red_both)
summary(m_rm_out_red)

summary(m_white_both)
summary(m_rm_out_white)



#6번
na_ave <- function(data,percentage)
{
  means <- colMeans(data)
  for (i in 1:10) {
    na_row<-sample(nrow(data),nrow(data)*percentage)
    na_col<-sample(ncol(data),nrow(data)*percentage,replace=TRUE)
    data[cbind(na_row,na_col)]<-NA
    for (j in 1:ncol(data)) {
      data[is.na(na_red_data[,j]), j] <- means[j]
    }
    m_na <<- lm(quality~.,data)  
    sum_data <- summary(m_na)
    if(i==1)
      total_value <<- sum_data$r.squared
    else
      total_value <<- c(total_value, sum_data$r.squared)
  }  
}

#red_data
summary(m_red)

na_ave(red_data,0.01)
mean(total_value)
sd(total_value)

na_ave(red_data,0.05)
mean(total_value)
sd(total_value)

na_ave(red_data,0.1)
mean(total_value)
sd(total_value)

#white data
summary(m_white)

na_ave(white_data,0.01)
mean(total_value)
sd(total_value)

na_ave(white_data,0.05)
mean(total_value)
sd(total_value)

na_ave(white_data,0.1)
mean(total_value)
sd(total_value)
