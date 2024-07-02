cox.stuart.test = function(x) {
  method = "Cox-Stuart test for trend analysis"
  leng = length(x)
  apross = round(leng)%%2
  if (apross == 1) {
    delete = (length(x) + 1)/2
    x = x[-delete]
  }
  half = length(x)/2
  x1 = x[1:half]
  x2 = x[(half + 1):(length(x))]
  difference = x1 - x2
  signs = sign(difference)
  signcorr = signs[signs != 0]
  pos = signs[signs > 0]
  neg = signs[signs < 0]
  if (length(pos) < length(neg)) {
    prop = pbinom(length(pos), length(signcorr), 0.5)
    names(prop) = "Increasing trend, p-value"
    rval <- list(method = method, statistic = prop)
    class(rval) = "htest"
    return(rval)
  } else {
    prop = pbinom(length(neg), length(signcorr), 0.5)
    names(prop) = "Decreasing trend, p-value"
    rval <- list(method = method, statistic = prop)
    class(rval) = "htest"
    return(rval)
  }
}

data = c(31.58, 42.94, 19.77, 24.29, 14.96, 12.91, 12.05, 12.11, 11.86)
cox.stuart.test(data)
model = c(18.42, 12.35, 29.94, 21.43, 31.43, 27.45, 27.81, 28.07, 27.17)
cox.stuart.test(model)
component = c(3.95, 10.00, 15.99, 13.10, 15.08, 17.91, 21.47, 20.93, 20.14)
cox.stuart.test(component)
Environment = c(36.84, 27.65, 23.84, 29.29, 23.70, 25.64, 20.83, 19.38, 21.38)
cox.stuart.test(Environment)
support = c(9.21, 7.06, 10.47, 11.90, 14.83, 16.09, 17.84, 19.50, 19.45)
cox.stuart.test(support)

support = c(0.00, 0.00, 3.23, 7.89, 7.22, 4.99, 5.62, 5.80, 5.53)
cox.stuart.test(support)
