
#NAME OF DATASET 
name <- 'Hollywood Most Profitable Stories movies data-Set'

#IMPORTING A DATASET AS DATAFRAME.
df_datasethollywood <- read.csv("C:/Users/mahsa/Desktop/Assignemt-Last/HollywoodsMostProfitableStories.csv")

#EXPLORATORY COMMANDS
df_head<-head(df_datasethollywood)
df_datasethollywood
df_summary<-summary(df_datasethollywood)
df_summary  # equivalent to the describe() in python but also gives # of NA
df_summary2<- as.data.frame(df_summary)
str(df_datasethollywood) #Structure of the data frame, equivalent to info() in python 

nrow(df_datasethollywood)
ncol(df_datasethollywood)

#CHECKING MISSING VALUES IN TABLE
colSums(is.na(df_datasethollywood)) #to get the sum of missing values for each columns 

#REMOVING MISSING VALUES IN TABLE

df_datasethollywood2<-df_datasethollywood
cleaned_data <- na.omit(df_datasethollywood2)

#Change Data Types
numeric_var <- 123
character_var <- as.character(numeric_var)

character_var <- "123"
numeric_var <- as.numeric(character_var)

factor_var <- factor(c("A", "B", "C"))
character_var <- as.character(factor_var)

numeric_var <- 123.45
integer_var <- as.integer(numeric_var)

date_string <- "2023-01-15"
date_variable <- as.Date(date_string)

#COLUMN SELECTION
df_datasethollywood2<-df_datasethollywood
df_datasethollywood2$Genre #column selection

df_datasethollywood2$Lead.Studio <-NULL #removing a column
data_cleaned<-na.omit(df_datasethollywood2, cols='Lead Studio') # per column 
colSums(is.na(data_cleaned))

names(df_datasethollywood2)  # equivalent to the column attribute in python 

install.packages("ggplot2")
install.packages("dplyr")

library(ggplot2)

library(dplyr)

# BAR PLOT OF GENDER DISTRIBUTION
ggplot(df_datasethollywood2, aes(x = Genre, fill = Genre)) +   geom_bar() +   labs(title = "Gendre Hollywoods", 
x = "Genre", y = "Profitability") +  theme_minimal()

# SCATTAR PLOT MATRIX
data <- data.frame(A=rnorm(50), B=rnorm(50), C=rnorm(50))
pairs(data, main="Scatter Plot Matrix", pch=19, col="purple")

# CUSTOMIZING LABELS AND TITLES
x <- c(1, 2, 3, 4, 5)
y <- c(2, 4, 1, 5, 7)
plot(x, y, main="Customized Plot", xlab="X-axis Label", ylab="Y-axis Label", col="brown")

# BOXPLOT
data <- list(A=c(1, 2, 3, 4, 5), B=c(2, 3, 4, 5, 6), C=c(3, 4, 5, 6, 7))
boxplot(data, main="Boxplot", xlab="Categories", ylab="Values", col=c("red", "green", "blue"))



#Rename Column Name

data_frame(df_datasethollywood2)

#RENAME COLUMN NAME
names(df_datasethollywood2)[names(df_datasethollywood2) == "Film"] <- "FILM"

names(df_datasethollywood2)[names(df_datasethollywood2) == "Main.Studio"] <- "LEAD.STUDIO"

#EXPORT CLEAN DATA TO YOUR PC
# Assuming 'clean_data' is your data frame

data_frame(cleaned_data)
write.csv(cleaned_data, file = "C:/Users/mahsa/Desktop/Assignemt-Last/CLEAN_DATA_BI.csv", row.names = FALSE)



