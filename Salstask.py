pping(weight):
      if weight <= 2:
              cost = weight * 1.5 + 20
                elif weight > 2 and weight <= 6:
                        cost = weight * 3 + 20
                          elif weight > 6 and weight <=10:
                                  cost = weight * 4 + 20
                                    elif weight > 10:
                                            cost = weight * 4.75 + 20
                                              return cost
                                          grpremium = 125

                                          def droneship(weight):
                                                if weight <= 2:
                                                        cost = weight * 4.5 
                                                          elif weight > 2 and weight <= 6:
                                                                  cost = weight * 9 
                                                                    elif weight > 6 and weight <=10:
                                                                            cost = weight * 12 
                                                                              elif weight > 10:
                                                                                      cost = weight * 14.25
                                                                                        return cost

                                                                                    def finalres(weight):
                                                                                          if groundshipping(weight) < grpremium and groundshipping(weight) < droneship(weight):
                                                                                                  return("Method of shipping is groundshipping with cost ",groundshipping(weight))
                                                                                                elif groundshipping(weight) > grpremium and droneship(weight) > grpremium:
                                                                                                        return("Method of shipping is Premium groundshipping with cost ", grpremium)
                                                                                                      else:
                                                                                                              return("Method of shipping is drone shipping with cost ",droneship(weight))

                                                                                                          print(finalres(3))
