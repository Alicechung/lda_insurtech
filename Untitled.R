library(arules)
library(arulesViz)
library(visNetwork)
library(igraph)
setwd("~/Desktop/lda_insurtech")
tr <- read.transactions("data.txt",
                        format = "basket",
                        sep = ",", 
                        cols = NULL)

#rules <- apriori(tr, parameter = list(supp = 0.5, conf = 0.9, target = "rules"))



#ig <- plot( subrules2, method="graph", control=list(type="items") )

rules <- apriori(tr, parameter=list(support=0.001, confidence=0.5))

#s <- as.data.frame(rules)
rule.list<-as.data.frame(inspect(rules))

subrules2 <- head(sort(rules, by="lift"), 1000)
#subrules2 <- head(sort(rules, by="lift"), 10)
#ss<-as.data.frame(inspect(subrules2))
res <- as(subrules2, "data.frame") 

ruledf <- data.frame(
  lhs = labels(lhs(subrules2)),
  rhs = labels(rhs(subrules2)), 
  subrules2@quality)

plot(subrules2, method = "paracoord")

write(rules, file = 'total.csv',sep =',',quote = TRUE,
      row.names = FALSE)
ig <- plot( subrules2, method="graph", control=list(type="items") )

# saveAsGraph seems to render bad DOT for this case
tf <- tempfile( )
saveAsGraph( subrules2, file = tf, format = "dot" )
# clean up temp file if desired
#unlink(tf)

# let's bypass saveAsGraph and just use our igraph
ig_df <- get.data.frame( ig, what = "both" )
nn1<-visNetwork(
  nodes = data.frame(
    id = ig_df$vertices$name
    ,value = ig_df$vertices$lift # could change to lift or confidence
    ,title = ifelse(ig_df$vertices$label == "",ig_df$vertices$name,
                    ig_df$vertices$label)
    ,ig_df$vertices
  )
  , edges = ig_df$edges
) %>%
  #visEdges( style = "arrow" ) %>%
  visOptions( highlightNearest = T )%>%
  visNodes(color = list(background = "lightblue", 
                        border = "blue",
                        highlight = "orange"),
           shadow = list(enabled = TRUE, size = 10)) 

visSave(nn1, file = "network2.html", selfcontained = TRUE, background = "white")
