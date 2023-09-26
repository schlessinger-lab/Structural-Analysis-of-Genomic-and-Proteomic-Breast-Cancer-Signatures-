# Fig 3A
# st_devplus<- c(3.700439718,2.478617973,2.104981654,0.603788675,0.840024227,1.031043847,1.048611919,1.388021777,1.212954835,0.229784024,0.703383296,-0.203108626,-0.372663205,0.095496231,-0.617005308,-0.688827336,-0.789397132,-0.83246,-1.350660407)
# st_devminus<- c(3.700439718,2.478617973,2.104981654,0.603788675,-0.218147679,-0.419841293,-0.488128769,-1.124685253,-1.137351767,-0.228361918,-1.083990802,-0.203108626,-0.468019699,-1.215355991,-0.699841986,-0.743125622,-0.789397132,-0.83246,-1.803562923)
# par(mar=c(5,15,1,1))
# barplot1 <- barplot(c(3.700439718,2.478617973,2.104981654,0.603788675,0.310938274,0.305601277,0.280241575,0.131668262,0.037801534,0.000711053,-0.190303753,-0.203108626,-0.420341452,-0.55992988,-0.658423647,-0.715976479,-0.789397132,-0.83246,-1.577111665) ,xlab="Average Log Ratio",beside=T , legend.text=T,col=c("blue") , xlim= c(-2,4), horiz=TRUE, las=1, names.arg=c("Immunoglobulin V-set Domain", "Disorder Binding", "Disorder", "310 Helix", "Turns", "High Curvature","Beta Bridge", "Length", "Alpha Helix", "Average Distance to Center of Mass", "Beta Bulge", "Maximum Distance to Center of Mass", "Nonconserved", "Conserved", "Aggregation Prone", "Negative", "Positive", "Globular", "Transmembrane Helix"))
# arrows(st_devplus, barplot1, st_devminus, barplot1, lwd = 1.5, angle = 90, code = 3, length = 0.05)

# #Fig 3B
# data<-data.frame(
#   # All = c(3.700439718,2.478617973,2.104981654,0.603788675,0.310938274,0.305601277,0.280241575,0.131668262,0.037801534,0.000711053,-0.190303753,-0.203108626,-0.420341452,-0.55992988,-0.658423647,-0.715976479,-0.789397132,-0.83246,-1.577111665),
#   "HER2 Negative"= c(0,2.478617973,2.104981654,0.603788675,0.25521678,0.305601277,0.03623631,1.020044352,0.868760402,0.068603167,0.078278674,0,-0.424366142,-0.918778845,0,-0.735173822,-0.789397132,0,-1.735932789),
#   "PR Negative" = c(3.700439718,0,0,0,0.47810276,0,0.7682521,0,0,-0.2029653,0,-0.2031086,-0.4048759,-0.7787659,-0.6291365,-0.6967791,0,0,0),
#   "ER Negative" = c(0,0,0,0,0,0,0,0,0,-0.2029653,0,-0.2031086,0,0,-0.6291365,-0.6967791,0,0,0)
#   )
# par(mar=c(5,15,1,1))
# barplot2 <- barplot(t(as.matrix(data)) , xlab="Average Log Ratio", beside=T , legend.text=T,col=c("red","light blue","light pink") , xlim= c(-2,4), horiz=TRUE, las=1, names.arg=c("Immunoglobulin V-set Domain", "Disorder Binding", "Disorder", "310 Helix", "Turns", "High Curvature","Beta Bridge", "Length", "Alpha Helix", "Average Distance to Center of Mass", "Beta Bulge", "Maximum Distance to Center of Mass", "Nonconserved", "Conserved", "Aggregation Prone", "Negative", "Positive", "Globular", "Transmembrane Helix"))

# Fig 4

# data<-data.frame(
#   mutated= c(4.169925001,3.906890596,3.892917278,3.730798919,3.48071418,3.13368589,2.962123737,2.753918308,2.74094417,2.736965594,2.569482866,2.522034326,2.503510211,2.483725316,2.469076352,2.377423081,2.291025905,2.257154523,2.180442772,2.148329951,2.041276117,1.998577799,1.858460503,1.789336244,1.592879238,1.539669337,1.338270825,1.262821965,0.991315046,0.976657973,0.534585279,0.282805902,-0.922542318,-1.612528422),
#   overexpressed = c(0,0,2.318448282,2.067080181,0,0.87968488,0,0,0,0,1.132557902,0,0,0.521445642,0,0.994058457,1.706126783,0,0,0.468131436,0,0,0,0,0,0,0,0,0.437171288,0.358831013,0,0,0,-2.430703133)
#   )
# label<-c("Immunoglobulin subtype 2","Immunoglobulin I-set","Disordered Binding","Disorder","Disorder Frequency","Sheet","Sheet Frequency","Beta Bulge Frequency","Beta Bulge","Immunoglobulin subtype","Loop","Globular","Negative Frequency","Length","Positive Frequency","Positive","Aggregation Prone","Aggregation Prone Frequency","Loop Frequency","Negative","High Curvature","High Curvature Frequency","Turn","Turn Frequency","Beta Bridge","Coiled Coil","Helix","310 Helix","Maximum Distance to Center of Mass","Average Distance to Center of Mass","Alpha Helix","Minimum Distance to Center of Mass","Conserved","Transmembrane Helix")
# barplot2 <- barplot(t(as.matrix(data)) , xlab="Average Log Ratio", beside=T , legend.text=T,col=c("red","blue") , xlim= c(-2.5,4.5), horiz=TRUE, las=1, names.arg=label)


# Fig 5
par(mar=c(5,15,1,1))
data <-c(3.700439718,2.906890596,1.421347761,-0.006103633,-0.200609637,-0.218648793,-0.409783857,-0.440829459,-0.466807105,-0.480089262,-0.498225401,-0.509043958,-0.58531265,-0.634213842,-0.642893045,-0.682145454,-0.6848459,-1.189613472,-1.52480527)
labels <- c("SH3 domain","Immunoglobulin-like domain","Transmembrane Helix","Conserved","Maximum Distance to Center of Mass","Average Distance to Center of Mass","Positive","310 Helix","High Curvature","Turns","Negative","Length","Globular","Aggregation Prone","Beta Bulge","Beta Bridge","Alpha Helix","Disorder","Disordered Binding")
st_devplus <- c(3.700439718,2.906890596,1.466154906,0.827118318,-0.179758436,-0.162549468,-0.409783857,-0.435018846,-0.343444841,-0.367016615,-0.490269678,-0.460762036,-0.509273047,-0.567223307,-0.504274613,-0.575363579,-0.6848459,-1.189613472,-1.52480527)
st_devminus <-c(3.700439718,2.906890596,1.376540616,-0.839325584,-0.221460838,-0.274748118,-0.409783857,-0.446640072,-0.590169369,-0.593161909,-0.506181124,-0.55732588,-0.661352253,-0.701204377,-0.781511477,-0.788927329,-0.6848459,-1.189613472,-1.52480527)
barplot1 <- barplot(data ,xlab="Average Log Ratio",beside=T , legend.text=T,col=c("blue") , horiz=TRUE, las=1, xlim= c(-2,4),names.arg=labels)
arrows(st_devplus, barplot1, st_devminus, barplot1, lwd = 1.5, angle = 90, code = 3, length = 0.05)


# Fig 6A
# data <-c(3.700439718,0.7682521,0.47810276,-0.4048759,-0.7787659)
# labels <- c("Immunoglobulin V-set domain","Beta Bridge","Turn","Nonconserved","Conserved")
# barplot1 <- barplot(data ,xlab="Average Log Ratio",beside=T , legend.text=T,col=c("blue") , horiz=TRUE, las=1, xlim= c(-2,4),names.arg=labels)
# 
# # Fig 6b
data <-c(-0.1920531,-0.4751184,-0.528455,-0.6054624,-0.6847855,-0.7351738,-0.7893971)
labels <- c("Average Distance to Center of Mass","Turn","High Curvature","Beta Bridge","Beta Bulge","Negative","Positive")
barplot1 <- barplot(data ,xlab="Average Log Ratio",beside=T , legend.text=T,col=c("blue") , horiz=TRUE, las=1, xlim= c(-2,4),names.arg=labels)


data <-c(-0.121123182298212, -0.119887284964298, -0.0998361451679082, -0.0996834833791379, 0.0255419579845659,0.181249445184875, 0.185923129270494,0.359793019946603)
labels <- c("Molecular Weight","Polar Surface Area", "Monoisotopic Molecular Weight", "Freebase Molecular Weight","Quantitative estimate of drug-likeness","logp","alogp", "logd")
par(mar=c(5,16,1,1)+.1)
barplot1 <- barplot(data ,xlab="Average Log Ratio",beside=T , legend.text=T,col=c("blue") , horiz=TRUE, las=1, xlim= c(-0.5,0.5),names.arg=labels)









