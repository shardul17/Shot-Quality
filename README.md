# Shot-Quality

While basketball is a team sport, many statistics, such as shooting percentages, can be skewed by team performance. With great coaching and a solid system, a player can take many open shots, thus resulting in a high offensive output. Conversely, a player with a poor system can be forced to take mainly contested shots, driving his offensive metrics down. In this project, I seeked to derive a  new "shooting percentage" statistic that allows scouts to understand how effective a singular player is given the opportunities he has by incorporating shot quality into a new rating metric.

To create this new proposed rating system, I assessed player quality based on the difference between individual performances and the league average percentages in each zone. I split up shot attempts into twelve categories; layups, mid-range, and three point shots in the four defensive ranges (0-2 Feet - Very Tight, 2-4 feet - Tight, 4-6 feet - Open, 6+ feet - Wide Open).

This data was obtained through the NBA.com advanced page by conducting a cross-analysis between the Closest Defender +10 and Closest Defender pages. The 3pt statistics among the two pages are identical, but the grey area arises in the 2pt shot category. The extra shots on the Closest Defender (CD) page when compared to the +10 page correspond to the layups, while all the 2pt shots in the CD+10 page can be classified as mid-range shots. We calculate the league averages by adding up the total field goal makes in each category and dividing those values by their respective field goal attempts. 

Figure 1 is a graphical representation of Devin Booker’s margins from league average in each shot category. 

![Image of Devin Booker's league margins](https://i.imgur.com/sC9Y7va.png)

The graph reveals a clear trend: field goal percentage essentially has a linear increase as the defensive intensity decreases for both mid-range and three point shots. Layups are the exception, but that can be attributed to the fact that a negligible amount of data exists for “Tight,” “Open,” and “Wide Open” layups. This trend allows us to argue that shot quality has a definitive general decline as defensive intensity decreases, a key factor that we account for in our proposed rating. 

Playing on a team that is largely deprived of various offensive weapons will force premier offensive players, like Booker, into a higher frequency of poor quality shots. A decent proportion of Booker’s shots come from the 2-4; in fact, 44.4% of his shots are contested in that manner, good for 3rd in the league. Booker connects at a much higher rate than league average from this range, but traditional offensive statistics cannot truly reflect how Booker attains these points. 

The quality multiplier is meant to represent the difficulty of a certain type of shot. For example, the league average FG% for all mid-range shots in the 2018-19 season was 40.7%. We take that value and divide it by the league FG% for each level of defensive intensity to attain a multiplier value, so a “Very Tight” mid-range shot would have a multiplier of 1.196, while a “Wide Open” mid-range shot would only have a multiplier of 0.907. This is meant to exacerbate the impact of “bad” shots; if a player takes and makes a hearty amount of contested shots, he would subsequently be rewarded with bump in the rating, but if a player misses a large amount of these “bad” shots, he would be penalized at a higher rate for not converting. 

Graphing each player’s value reveals an interesting trend.

![Image of EFG% asjutment graph](https://i.imgur.com/PDXjVzA.png)

Below is a table of the new EFG% coupled with the original EFG%. 

| Name | Adjusted EFG% | Original EFG% |
|     :---:    |     :---:      |     :---:     |
|  Joe Harris  |  64.7  |  62.2  |
|  Danny Green  |  64.0  |  62.2  |
|  Stephen Curry  |  61.3  |  60.4  |
|  Davis Bertans  |  61.3  |  61.0  |
|  Seth Curry  |  59.7  |  57.7  |
|  Kyle Korver  |  59.0  |  55.9  |
|  Wayne Ellington  |  58.4  |  55.4  |
|  Landry Shamet  |  57.9  |  58.1  |
|  Bryn Forbes  |  57.2  |  56.8  |
|  JJ Redick  |  56.8  |  55.7  |
|  James Harden  |  56.5  |  54.1  |
|  Malik Beasley  |  56.3  |  58.4  |
|  D.J. Augustin  |  56.0  |  56.6  |
|  Kyrie Irving  |  55.9  |  55.7  |
|  E'Twaun Moore  |  55.8  |  55.3  |
|  Terrence Ross  |  55.8  |  53.4  |
|  Buddy Hield  |  55.7  |  56.0  |
|  Rudy Gay  |  55.4  |  55.4  |
|  Doug McDermott  |  55.4  |  59.0  |
|  Vince Carter  |  55.4  |  55.0  |
|  Danilo Gallinari  |  55.2  |  55.4  |
|  Klay Thompson  |  55.1  |  55.3  |
|  Kevin Durant  |  54.9  |  57.1  |
|  Joe Ingles  |  54.7  |  56.5  |
|  Tony Snell  |  54.7  |  56.4  |
|  Monte Morris  |  54.6  |  56.0  |
|  Patty Mills  |  54.5  |  54.5  |
|  Darius Miller  |  54.4  |  52.8  |
|  Mike Scott  |  54.1  |  52.0  |
|  Malcolm Brogdon  |  54.0  |  57.5  |
|  Quinn Cook  |  54.0  |  55.7  |
|  Reggie Bullock  |  54.0  |  53.7  |
|  Gerald Green  |  53.9  |  53.5  |
|  Bojan Bogdanovic  |  53.5  |  57.5  |
|  Tobias Harris  |  53.2  |  54.9  |
|  Nemanja Bjelica  |  53.1  |  56.6  |
|  Paul George  |  53.1  |  52.9  |
|  Nicolas Batum  |  52.9  |  55.3  |
|  Juancho Hernangomez  |  52.9  |  54.5  |
|  CJ McCollum  |  52.9  |  52.7  |
|  Taurean Prince  |  52.7  |  54.5  |
|  Patrick Beverley  |  52.7  |  52.4  |
|  Luke Kennard  |  52.6  |  54.0  |
|  Brook Lopez  |  52.5  |  57.1  |
|  Khris Middleton  |  52.5  |  51.9  |
|  Marco Belinelli  |  52.3  |  52.0  |
|  Pascal Siakam  |  52.3  |  59.1  |
|  Thomas Bryant  |  52.2  |  64.8  |
|  Chris Paul  |  52.1  |  50.8  |
|  PJ Tucker  |  52.0  |  53.5  |
|  D'Angelo Russell  |  52.0  |  51.2  |
|  Kemba Walker  |  52.0  |  51.1  |
|  Karl-Anthony Towns  |  52.0  |  57.2  |
|  Otto Porter Jr.  |  51.9  |  54.6  |
|  Damian Lillard  |  51.8  |  52.2  |
|  Derrick Rose  |  51.5  |  51.8  |
|  Royce O'Neale  |  51.4  |  57.4  |
|  Kentavious Caldwell-Pope  |  51.3  |  53.0  |
|  Marcus Smart  |  51.3  |  53.3  |
|  Langston Galloway  |  51.2  |  50.3  |
|  Eric Gordon  |  51.2  |  52.5  |
|  Spencer Dinwiddie  |  51.2  |  51.7  |
|  Marvin Williams  |  51.1  |  52.9  |
|  Al Horford  |  51.1  |  58.6  |
|  Steven Adams  |  51.1  |  59.5  |
|  Kawhi Leonard  |  51.1  |  54.6  |
|  Ryan Arcidiacono  |  51.0  |  54.4  |
|  Nik Stauskas  |  50.8  |  50.6  |
|  Jahlil Okafor  |  50.8  |  58.7  |
|  Jeremy Lamb  |  50.8  |  49.9  |
|  Jamal Crawford  |  50.7  |  47.4  |
|  Maxi Kleber  |  50.7  |  55.3  |
|  Kevin Huerter  |  50.6  |  52.2  |
|  Devin Booker  |  50.6  |  52.1  |
|  Norman Powell  |  50.6  |  56.8  |
|  Clint Capela  |  50.6  |  64.8  |
|  Dewayne Dedmon  |  50.6  |  57.1  |
|  Rudy Gobert  |  50.5  |  66.9  |
|  Josh Richardson  |  50.5  |  49.2  |
|  Blake Griffin  |  50.5  |  53.2  |
|  Kelly Olynyk  |  50.5  |  56.3  |
|  Damyean Dotson  |  50.5  |  50.6  |
|  Yogi Ferrell  |  50.5  |  51.1  |
|  JaMychal Green  |  50.4  |  55.8  |
|  Marcus Morris  |  50.4  |  53.3  |
|  Reggie Jackson  |  50.3  |  50.4  |
|  Terrance Ferguson  |  50.3  |  55.2  |
|  Sterling Brown  |  50.3  |  55.0  |
|  Bradley Beal  |  50.2  |  54.0  |
|  Jerami Grant  |  50.1  |  56.7  |
|  Jordan Clarkson  |  50.1  |  50.9  |
|  Pat Connaughton  |  50.1  |  56.0  |
|  Mike Muscala  |  50.0  |  52.5  |
|  Rodney McGruder  |  49.9  |  48.9  |
|  John Collins  |  49.8  |  59.3  |
|  T.J. McConnell  |  49.6  |  54.2  |
|  Jeff Green  |  49.5  |  55.5  |
|  Jonas Jerebko  |  49.5  |  55.6  |
|  CJ Miles  |  49.4  |  46.8  |
|  Kyle Lowry  |  49.4  |  51.8  |
|  Wesley Matthews  |  49.4  |  50.7  |
|  Donovan Mitchell  |  49.3  |  49.3  |
|  Fred VanVleet  |  49.3  |  50.3  |
|  Dario Saric  |  49.0  |  52.2  |
|  Jake Layman  |  49.0  |  57.9  |
|  Jaylen Brown  |  49.0  |  52.5  |
|  Darren Collison  |  49.0  |  52.7  |
|  Mikal Bridges  |  48.9  |  52.3  |
|  Bogdan Bogdanovic  |  48.9  |  49.6  |
|  Bam Adebayo  |  48.8  |  57.9  |
|  Taj Gibson  |  48.8  |  57.6  |
|  Mike Conley  |  48.8  |  50.7  |
|  Myles Turner  |  48.7  |  53.6  |
|  Derrick White  |  48.7  |  52.3  |
|  Terry Rozier  |  48.6  |  47.7  |
|  Jamal Murray  |  48.5  |  50.2  |
|  LeBron James  |  48.4  |  56.0  |
|  Justin Holiday  |  48.3  |  49.0  |
|  Tomas Satoransky  |  48.3  |  54.5  |
|  Harrison Barnes  |  48.2  |  50.4  |
|  Lance Stephenson  |  48.1  |  51.0  |
|  Rodney Hood  |  48.1  |  49.8  |
|  Justise Winslow  |  48.1  |  49.7  |
|  Domantas Sabonis  |  48.0  |  59.6  |
|  Jae Crowder  |  48.0  |  50.8  |
|  Nikola Vucevic  |  47.9  |  54.9  |
|  Kevon Looney  |  47.9  |  62.7  |
|  Justin Jackson  |  47.9  |  53.7  |
|  Noah Vonleh  |  47.8  |  52.3  |
|  Dwyane Wade  |  47.8  |  47.8  |
|  Serge Ibaka  |  47.8  |  55.7  |
|  Kelly Oubre Jr.  |  47.7  |  51.0  |
|  Shai Gilgeous-Alexander  |  47.7  |  51.2  |
|  Trevor Ariza  |  47.6  |  49.8  |
|  Lauri Markkanen  |  47.5  |  50.6  |
|  Montrezl Harrell  |  47.4  |  61.7  |
|  Luka Doncic  |  47.4  |  49.7  |
|  Garrett Temple  |  47.4  |  51.3  |
|  OG Anunoby  |  47.2  |  53.6  |
|  Trey Burke  |  47.2  |  48.2  |
|  Cedi Osman  |  47.1  |  50.4  |
|  Tim Hardaway Jr.  |  47.1  |  47.4  |
|  Zach LaVine  |  47.0  |  52.0  |
|  Emmanuel Mudiay  |  46.9  |  49.3  |
|  Lou Williams  |  46.9  |  47.1  |
|  Andre Iguodala  |  46.9  |  57.9  |
|  Austin Rivers  |  46.9  |  49.7  |
|  Shabazz Napier  |  46.7  |  47.6  |
|  Julius Randle  |  46.7  |  55.5  |
|  Thaddeus Young  |  46.6  |  55.7  |
|  Jalen Brunson  |  46.6  |  52.3  |
|  Evan Fournier  |  46.6  |  50.9  |
|  Alex Len  |  46.5  |  55.1  |
|  Avery Bradley  |  46.5  |  47.9  |
|  Jaren Jackson Jr.  |  46.4  |  54.9  |
|  Eric Bledsoe  |  46.4  |  54.8  |
|  DeMarre Carroll  |  46.4  |  48.7  |
|  Nikola Jokic  |  46.3  |  54.5  |
|  Jayson Tatum  |  46.3  |  50.6  |
|  George Hill  |  46.3  |  51.6  |
|  DeAndre Jordan  |  46.3  |  64.1  |
|  Allonzo Trier  |  46.2  |  49.8  |
|  Zach Collins  |  46.2  |  52.3  |
|  Al-Farouq Aminu  |  46.2  |  51.4  |
|  JaVale McGee  |  46.2  |  62.5  |
|  Marc Gasol  |  46.1  |  50.5  |
|  Ersan Ilyasova  |  46.0  |  51.4  |
|  Paul Millsap  |  46.0  |  52.8  |
|  Iman Shumpert  |  46.0  |  48.1  |
|  Gary Harris  |  46.0  |  48.8  |
|  Jabari Parker  |  45.9  |  53.3  |
|  Richaun Holmes  |  45.9  |  60.8  |
|  Larry Nance Jr.  |  45.8  |  55.4  |
|  Malik Monk  |  45.7  |  48.0  |
|  Tyler Johnson  |  45.6  |  49.8  |
|  Miles Bridges  |  45.6  |  52.7  |
|  Josh Hart  |  45.5  |  50.6  |
|  Brandon Ingram  |  45.5  |  51.8  |
|  Torrey Craig  |  45.4  |  52.6  |
|  Ed Davis  |  45.3  |  61.6  |
|  Anthony Davis  |  45.3  |  54.0  |
|  Jrue Holiday  |  45.2  |  52.3  |
|  Markieff Morris  |  45.2  |  49.2  |
|  Collin Sexton  |  45.2  |  48.0  |
|  Dennis Schroder  |  45.1  |  47.0  |
|  Maurice Harkless  |  45.1  |  53.0  |
|  Aaron Gordon  |  45.0  |  50.7  |
|  Alec Burks  |  45.0  |  46.9  |
|  Gordon Hayward  |  44.8  |  52.7  |
|  Ian Clark  |  44.8  |  48.0  |
|  Gorgui Dieng  |  44.8  |  52.7  |
|  Jeremy Lin  |  44.7  |  49.1  |
|  Dirk Nowitzki  |  44.6  |  44.4  |
|  Giannis Antetokounmpo  |  44.5  |  59.9  |
|  Marvin Bagley III  |  44.5  |  52.5  |
|  Hassan Whiteside  |  44.5  |  57.2  |
|  Dorian Finney-Smith  |  44.4  |  50.7  |
|  Deandre Ayton  |  44.4  |  58.5  |
|  Dennis Smith Jr.  |  44.4  |  47.9  |
|  James Johnson  |  44.4  |  49.9  |
|  Enes Kanter  |  44.1  |  55.6  |
|  Kyle Kuzma  |  44.1  |  51.5  |
|  Trae Young  |  44.1  |  48.0  |
|  Dwight Powell  |  44.1  |  63.7  |
|  Jonathan Isaac  |  44.0  |  49.9  |
|  Robin Lopez  |  43.8  |  57.5  |
|  Derrick Jones Jr.  |  43.7  |  53.7  |
|  LaMarcus Aldridge  |  43.6  |  52.2  |
|  Wayne Selden  |  43.6  |  46.3  |
|  Frank Jackson  |  43.4  |  49.3  |
|  Devin Harris  |  43.3  |  47.0  |
|  De'Aaron Fox  |  43.3  |  49.7  |
|  Mario Hezonja  |  43.3  |  45.7  |
|  DeMar DeRozan  |  43.2  |  48.3  |
|  Cory Joseph  |  43.2  |  46.3  |
|  Kevin Knox  |  43.0  |  43.8  |
|  Kent Bazemore  |  43.0  |  47.2  |
|  Antonio Blakeney  |  42.7  |  46.5  |
|  Evan Turner  |  42.7  |  47.3  |
|  Jimmy Butler  |  42.4  |  49.9  |
|  Shelvin Mack  |  42.1  |  46.2  |
|  Josh Jackson  |  42.0  |  45.6  |
|  Rodions Kurucs  |  41.9  |  51.4  |
|  Andrew Wiggins  |  41.6  |  46.1  |
|  Joel Embiid  |  41.4  |  51.7  |
|  Jusuf Nurkic  |  41.3  |  51.0  |
|  Tyus Jones  |  41.1  |  46.0  |
|  Tony Parker  |  41.1  |  47.4  |
|  Ricky Rubio  |  41.1  |  45.8  |
|  Ish Smith  |  41.1  |  46.4  |
|  Mason Plumlee  |  41.0  |  59.5  |
|  Derrick Favors  |  40.9  |  60.0  |
|  Tyreke Evans  |  40.9  |  44.8  |
|  Ben Simmons  |  40.8  |  56.3  |
|  DeAndre' Bembry  |  40.7  |  48.7  |
|  Ante Zizic  |  40.6  |  55.3  |
|  Harry Giles III  |  40.4  |  50.3  |
|  Stanley Johnson  |  40.4  |  45.9  |
|  Willie Cauley-Stein  |  40.0  |  55.7  |
|  Michael Kidd-Gilchrist  |  39.9  |  50.0  |
|  Draymond Green  |  39.6  |  50.1  |
|  Russell Westbrook  |  39.6  |  46.8  |
|  Delon Wright  |  39.0  |  47.8  |
|  Josh Okogie  |  38.5  |  44.5  |
|  Andre Drummond  |  38.5  |  53.6  |
|  Trey Lyles  |  37.5  |  47.0  |
|  Shaquille Harrison  |  37.1  |  46.0  |
|  Jarrett Allen  |  36.3  |  59.5  |
|  Ivica Zubac  |  35.4  |  55.9  |
|  Jonathon Simmons  |  35.0  |  42.0  |
|  Bruce Brown  |  34.2  |  43.6  |
|  Rondae Hollis-Jefferson  |  26.6  |  42.0  |



