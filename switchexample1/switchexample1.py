func dayType (day: String) -> String {
    var typeOfDay: String = ""
    for var i = 0; i < daysOfWeek.count; i++ {
        if(day == daysOfWeek[i]){
          // process the array index
            switch i {
                case 0...4: typeOfDay = "It's a weekday"
                case 5, 6: typeOfDay = "It's weekend!"
                default: typeOfDay = "Unlikely to be a day"
            } // end switch
        } else {
            typeOfDay = "Not a day"
        } // end if
    }// end for
    return typeOfDay
} // end func
