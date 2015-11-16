setwd("~/Desktop/15fall/Thesis/twitter/NewYorker")
profiles <- read.csv("data/test1.csv")

ids <- unique(profiles$id) # 9999 unique ids

newdata <- data.frame()
for (i in 1:495020) {
    if (!(profiles$id[i] %in% newdata$id)) newdata <- rbind(newdata, profiles[i, ])
}

write.csv(newdata, "data/nondup.csv")

englishSpeaker <- newdata[grepl("en", newdata$lang), ]

write.csv(englishSpeaker, "data/nondupeng.csv")
