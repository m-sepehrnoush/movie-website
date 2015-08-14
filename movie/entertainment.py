import fresh_tomatoes
import media

"""Creates movie objects and feeds them to
   fresh_tomatoes module as a list.
"""

# Instantiating movie objects
lock_stock = media.Movie("Lock, Stock and Two Smoking Barrels",
                         "Lock, Stock and Two Smoking Barrels is a "+
                         "1998 British crime comedy film written and"+
                         " directed by Guy Ritchie. The story is a "+
                         "heist film involving a self-confident young"+
                         " card sharp who loses &pound500,000 to a "+
                         "powerful crime lord in a rigged game of "+
                         "three card brag. To pay off his debts, he"+
                         " and his friends decide to rob a small-time"+
                         " gang who happen to be operating out of the"+
                         " flat next door.",
                         "https://upload.wikimedia.org/"+
                         "wikipedia/en/e/e9/"+
                         "Lock%2C_Stock_and_Two_Smoking_Barrels_2.jpg",
                         "https://www.youtube.com/watch?v=Y8MXn5No1Jc")

leon = media.Movie("Leon: The Professional",
                   "Leon: The Professional (French: Leon; also known"+
                   " as The Professional) is a 1994 English-language "+
                   "French thriller film written and directed by Luc "+
                   "Besson. It stars Jean Reno and Gary Oldman, and "+
                   "features the motion picture debut of Natalie "+
                   "Portman. In the film Leon (Reno), a professional "+
                   "hitman, reluctantly takes in 12-year-old girl "+
                   "Mathilda (Portman), after her family is murdered "+
                   "by corrupt Drug Enforcement Administration agent "+
                   "Norman Stansfield (Oldman). Leon and Mathilda form"+
                   " an unusual relationship, as she becomes his "+
                   "protegee and learns the hitman's trade.",
                   "https://upload.wikimedia.org/"+
                   "wikipedia/en/thumb/0/03/Leon-poster.jpg/"+
                   "220px-Leon-poster.jpg",
                   "https://www.youtube.com/watch?v=yRABrgRcn5Y")

usual_suspects = media.Movie("The Usual Suspects",
                             "The Usual Suspects is a 1995 American "+
                             "neo-noir crime thriller film directed by"+
                             " Bryan Singer and written by Christopher"+
                             " McQuarrie. It stars Stephen Baldwin, "+
                             "Gabriel Byrne, Benicio del Toro, Kevin "+
                             "Pollak, Chazz Palminteri, Pete "+
                             "Postlethwaite and Kevin Spacey. The film"+
                             " follows the interrogation of Roger "+
                             "'Verbal' Kint, a small-time con man who "+
                             "is one of only two survivors of a "+
                             "massacre and fire on a ship docked at "+
                             "the Port of Los Angeles. He tells an "+
                             "interrogator a convoluted story about "+
                             "events that led him and his partners in"+
                             " crime to the boat, and about a "+
                             "mysterious mob boss known as Keyser Soze"+
                             " who commissioned their work. Using "+
                             "flashback and narration, Kint's story "+
                             "becomes increasingly complex.",
                             "https://upload.wikimedia.org/wikipedia"+
                             "/en/thumb/9/9c/Usual_suspects_ver1.jpg"+
                             "/220px-Usual_suspects_ver1.jpg",
                             "https://www.youtube.com/"+
                             "watch?v=oiXdPolca5w")

terminator_two = media.Movie("Terminator 2: Judgment Day",
                             "Terminator 2: Judgment Day (also "+
                             "referred to as simply Terminator 2 or "+
                             "T2) is a 1991 American science fiction "+
                             "action film co-written, produced and "+
                             "directed by James Cameron. The film "+
                             "stars Arnold Schwarzenegger, Linda "+
                             "Hamilton, Robert Patrick and Edward "+
                             "Furlong. It is the sequel to the 1984 "+
                             "film The Terminator, and the second "+
                             "installment in the Terminator franchise."+
                             " Terminator 2 follows Sarah Connor "+
                             "(Hamilton) and her ten-year-old son John"+
                             " (Furlong) as they are pursued by a new,"+
                             " more advanced Terminator, the liquid "+
                             "metal, shapeshifting T-1000 (Patrick), "+
                             "sent back in time to kill John Connor "+
                             "and prevent him from becoming the leader"+
                             " of the human resistance. A second, less"+
                             " advanced Terminator (Schwarzenegger) is"+
                             " also sent back in time to protect John.",
                             "https://upload.wikimedia.org/wikipedia/"+
                             "en/8/85/Terminator2poster.jpg",
                             "https://www.youtube.com/"+
                             "watch?v=eajuMYNYtuY")

v_for_vendetta = media.Movie("V for Vendetta",
                             "V for Vendetta is a graphic novel "+
                             "written by Alan Moore and illustrated by"+
                             " David Lloyd (with additional art by "+
                             "Tony Weare), published by Vertigo, an "+
                             "imprint of DC Comics. The story depicts "+
                             "a dystopian and post-apocalyptic near-"+
                             "future history version of the United "+
                             "Kingdom in the 1990s, preceded by a "+
                             "nuclear war in the 1980s, which has left"+
                             " most of the world destroyed. The "+
                             "fascist Norsefire party has "+
                             "exterminated its opponents in "+
                             "concentration camps and rules the "+
                             "country as a police state. The comics "+
                             "follow its titular character and "+
                             "protagonist, V, an anarchist "+
                             "revolutionary dressed in a Guy Fawkes "+
                             "mask, as he begins an elaborate and "+
                             "theatrical revolutionist campaign to "+
                             "murder his former captors, bring down "+
                             "the government and convince the people "+
                             "to rule themselves, while inspiring a "+
                             "young woman, Evey Hammond, to be his "+
                             "protege.",
                             "https://upload.wikimedia.org/wikipedia"+
                             "/en/thumb/c/c0/V_for_vendettax.jpg/"+
                             "250px-V_for_vendettax.jpg",
                             "https://www.youtube.com/"+
                             "watch?v=k_13fFIrhPk")

inglourious_basterds = media.Movie("Inglourious Basterds",
                                   "Inglourious Basterds is a 2009 "+
                                   "American war film written and "+
                                   "directed by Quentin Tarantino and "+
                                   "starring Brad Pitt, Christoph "+
                                   "Waltz, Diane Kruger, Michael "+
                                   "Fassbender and Eli Roth. The film "+
                                   "tells the fictional alternate "+
                                   "history story of two plots to "+
                                   "assassinate Nazi Germany's "+
                                   "political leadership, one planned "+
                                   "by a young French Jewish cinema "+
                                   "proprietor, and the other by a "+
                                   "team of Jewish-American soldiers "+
                                   "led by First Lieutenant Aldo Raine"+
                                   ". The film's title was inspired by"+
                                   " director Enzo G. Castellari's "+
                                   "macaroni combat film, The "+
                                   "Inglorious Bastards (1978).",
                                   "https://upload.wikimedia.org/"+
                                   "wikipedia/en/c/c3/"+
                                   "Inglourious_Basterds_poster.jpg",
                                   "https://www.youtube.com/"+
                                   "watch?v=KnrRy6kSFF0")

django_unchained = media.Movie("Django Unchained",
                               "Django Unchained is a 2012 American "+
                               "western film written and directed by "+
                               "Quentin Tarantino. Set in the Old West"+
                               " and Antebellum South, it is a highly "+
                               "stylized variation of the spaghetti "+
                               "Western. The film stars Jamie Foxx, "+
                               "Christoph Waltz, Leonardo DiCaprio, "+
                               "Kerry Washington, and Samuel L. "+
                               "Jackson. The story is set in early "+
                               "winter and the following spring, "+
                               "during the antebellum era of the Deep"+
                               " South, with preliminary scenes taking"+
                               " place in Old West Texas. The film "+
                               "follows Django (Foxx), an "+
                               "African-American slave, and Dr. King "+
                               "Schultz (Waltz), an English-speaking "+
                               "German bounty hunter posing as a "+
                               "traveling dentist. Schultz buys and "+
                               "then promises to free Django in "+
                               "exchange for his help in collecting a "+
                               "large bounty on three outlaws. Schultz"+
                               " subsequently promises to teach Django"+
                               " bounty hunting, and split the "+
                               "bounties with him, if Django assists "+
                               "him in hunting down other outlaws "+
                               "throughout the winter. He further "+
                               "offers to help Django to locate and "+
                               "free his long-lost wife (Washington)"+
                               " from her cruel plantation owner "+
                               "(DiCaprio).",
                               "https://upload.wikimedia.org/wikipedia"+
                               "/en/8/8b/Django_Unchained_Poster.jpg",
                               "https://www.youtube.com/"+
                               "watch?v=eUdM9vrCbow")

seven = media.Movie("SE7EN",
                    "Seven (sometimes stylized as SE7EN) is a 1995 "+
                    "American neo-noir crime psychological thriller "+
                    "film directed by David Fincher, and stars Brad "+
                    "Pitt, Morgan Freeman, Gwyneth Paltrow, John C. "+
                    "McGinley, R. Lee Ermey and Kevin Spacey. The film"+
                    " was based on a screenplay by Andrew Kevin Walker"+
                    ". The film follows a newly transferred David "+
                    "Mills (Pitt) and the soon-to-retire William "+
                    "Somerset (Freeman), two homicide detectives who "+
                    "become deeply involved in the case of a sadistic "+
                    "serial killer whose meticulously planned murders "+
                    "correspond to the seven deadly sins: gluttony, "+
                    "greed, sloth, wrath, pride, lust and envy.",
                    "https://upload.wikimedia.org/wikipedia/"+
                    "en/6/68/Seven_%28movie%29_poster.jpg",
                    "https://www.youtube.com/watch?v=-Jxp1AqoSeM")

pulp_fiction = media.Movie("Pulp Fiction",
                           "Pulp Fiction is a 1994 American black "+
                           "comedy crime film written and directed by"+
                           " Quentin Tarantino, from a story by "+
                           "Tarantino and Roger Avary. The film is "+
                           "known for its eclectic dialogue, ironic "+
                           "mix of humor and violence, nonlinear "+
                           "storyline, and a host of cinematic "+
                           "allusions and pop culture references. "+
                           "The film was nominated for seven Oscars,"+
                           " including Best Picture; Tarantino and "+
                           "Avary won for Best Original Screenplay. It"+
                           " was also awarded the Palme d'Or at the "+
                           "1994 Cannes Film Festival. A major "+
                           "critical and commercial success, it "+
                           "revitalized the career of its leading man,"+
                           " John Travolta, who received an Academy "+
                           "Award nomination, as did co-stars Samuel "+
                           "L. Jackson and Uma Thurman.",
                           "https://upload.wikimedia.org/wikipedia/"+
                           "en/8/82/Pulp_Fiction_cover.jpg",
                           "https://www.youtube.com/"+
                           "watch?v=5ZAhzsi1ybM")

fight_club = media.Movie("Fight Club",
                         "Fight Club is a 1999 film based on the 1996 "+
                         "novel of the same name by Chuck Palahniuk. "+
                         "The film was directed by David Fincher, and "+
                         "stars Brad Pitt, Edward Norton and Helena "+
                         "Bonham Carter. Norton plays the unnamed "+
                         "protagonist, an "'everyman'" who is "+
                         "discontented with his white-collar job. He "+
                         "forms a ""fight club"" with soap maker Tyler"+
                         " Durden, played by Pitt, and they are joined"+
                         " by men who also want to fight "+
                         "recreationally. The narrator becomes "+
                         "embroiled in a relationship with Durden and "+
                         "a dissolute woman, Marla Singer, played by"+
                         " Bonham Carter.",
                         "https://upload.wikimedia.org/wikipedia/"+
                         "en/f/fc/Fight_Club_poster.jpg",
                         "https://www.youtube.com/watch?v=_XgQA9Ab0Gw")

# Create a list of movie objects
movies = [lock_stock, leon, usual_suspects, terminator_two,
          v_for_vendetta, inglourious_basterds, django_unchained,
          seven, pulp_fiction, fight_club]

# Show movies in a webpage
fresh_tomatoes.open_movies_page(movies)
