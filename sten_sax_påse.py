#Vi importerar random modulen
import random
import time
import getpass
#Vi definerar variablerna
val1 = 0
val2 = 0
runda = 1
loop = True
point1 = 0
point2 = 0
pc = 0
rock = '''
                                         /((####(*,/((*((*(/                   
                                      ../,./(((((((((((/((#(#(*                
                                  ,*/#/*/(#(*/###(((//*/#%%%%%#,               
                               //(#%(##(%##(((((#((/(###(##/(#%%(              
                             ,///((((((STEN((((*.*(#(((/*/(((/##%,             
                         .((#(*/#/##(///(((//##(##(/#((*/@((##(            
                      *((//*(//(#(#((/(%%##(((#//((*%#(%&%&//#%((#,          
                   ,//((#(((//,*(#%###(%&%&%%##((((/,*#*(((/(((*/((%##.        
                 ,*,*///(((/**/(#/(/(#(%(#/((##((*#((%&&&%%%%%@&&((&&&.        
               .,/#.*//**##/(*/&&%/(##(#%(##(/**/(%#%######//#*%%%%%@&(        
             ./#(**/(( ((*/(/,*/((((///%%###(((((/(%(#(%%%%%&%#/%%%%%&%.       
           ,/(/#((((#(,////(,,(###((/#(%#%(/*(###&%/%@#%@&&%%%&&&%&&%(       
          *///,(/(((/*/(**,*,(/*,*,((((%%#%#&&&&%#####&%%##%/%%&&&%%#%       
        ./(///*/((///#%(,***///#(//####(#&%@&&%&#%&STEN&&&%##&@@&@&%%%#      
        ///(*((.,,((((/,**///(////#&&%%%&&&%&&&&&&&&&&&%&&&%@&%@@@@&%&%%&      
        /(///,(#(*,*.,*.,#%((((##%&&&&&&%&&&&&&&%&@%%%%%%%%%%##&@@@&%&%#%/     
       .*///*(#//*//*/#((,,/###%%&%&&&%%&&&%&%&&&&&&&%%&&%%%%&&&&%%%%%#(.    
       .*//,,*/,*/##%###%%#//%#(&&&%%&%&&&STEN%&&&%%%&&&&%%#%%%%%%%%#%%      
        *////#(/(##///(###(#%#(%&%%%%%%&&&&&&&&%&&&%%#%#((#(%%%%%&&%%&%/     
         ,//#**(/*%####(##%#@##&%&&&&&%%&&&&&&(%@&%%%#%%%#%%(%%%&%&&&%#,       
           /((/**/(#####/#(/(%&@&&&&STEN&&&&&&%%%&%&&&&&&&&%#%%%%%%%(/         
            ,///***(//(####%&&&&%##%%&&%&&@&&&%&%&&&&&&%%%%&%####/.            
              *((**////(#####%%%%%%STEN@&@&&&@&&&&&&%%%%%%###/.                
               .*/(//*/#((((%##%%%%%&&&&&&%%&&%%%%%#(/*,..                     
                 .((((######%###%&&@&&%###(,                                   
                   ./###%%###%%%%####(/.                                       
                          ..**,,.
'''
paper = '''
                                                                               
    ,&&&&&&&&&&&&                                           @@@@@@@@@@@@@@,    
    .@@,,,,,,,,@@(                                         @@@,,,,,,,,,,/@@    
    .@@        @@(                                         @@&          ,@@    
    .@@        @@(                                         @@&          ,@@    
    .@@        @@(                                         @@&          ,@@    
    .@@        @@(                                         @@&          ,@@    
    .@@        @@(                                         @@&          ,@@    
    .@@        @@(                                         @@&          ,@@    
    .@@        @%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&          ,@@    
    .@@                                                                 ,@@    
    .@@                                                                 ,@@    
    .@@                                                                 ,@@    
    .@@                                                                 ,@@    
    .@@                                                                 ,@@    
    .@@                                                                 ,@@    
    .@@                                                                 ,@@    
    .@@            @@@  *@   @@@  @@@   .@@( /@@*  @@@@ &@@@            ,@@    
    .@@           @@@.   @@ @@@@  .@@@ ,@@@   @@@* @@@@  @@@/           ,@@    
    .@@          (@@@       @@@%   @@@.@@@@   @@@@ @@@@  @@@            ,@@    
    .@@          /@@@     # @@@%   @@@ &@@@   @@@@ @@@@                 ,@@    
    .@@           @@@(   .@ .@@@  *@@@  @@@   @@@  @@@@                 ,@@    
    .@@             @@@@@,    (@@@@&      @@@@@.   @@@@                 ,@@    
    .@@                                                                 ,@@    
    .@@                                                                 ,@@    
    .@@                                                                 ,@@    
    .@@                                                                 ,@@    
    .@@       ...................................................       ,@@    
    .@@       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%       ,@@    
    .@@                                                                 ,@@    
    .@@                                                                 ,@@    
    .@@       ...................................................       ,@@    
    .@@        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       ,@@    
    .@@                                                                 ,@@    
    .@@                                                                 ,@@    
    .@@                                                                 ,@@    
    .@@                                                                 ,@@    
     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@    
                                                                               
'''
scissors = '''
             **                                                                
             .*/                                                               
       **     .//*                                                             
        ./*.   /(/(                                                            
          (/*,  ////.                                                          
           ,**** (////                                                         
             /***,(((((                                                        
              /****,###(,                                                      
               ./**,,,,(#(                                                     
                 /*,,,,..(#                                                    
                   ,,,.,.../*                                                  
                    *,........                                                 
                     .,...#* ...                                               
                       *,*&%(*....                                             
                        &,..........                                           
                         &(.........,(@&%                                      
                          (#%%%#   .#%@&&&&,                                 
                           /(((      %@@&@@@@@&&%*                             
                           @&(/        (@@@@@@@@&&&%%.                       
                           &@@@&,        *@@@@&@@@@@@@@@@@@&&%((%,             
                           %@@@@%/         .@@@@&&,&@@@@@@&(/(&@@@&/.          
                           ,&@@@&,,           @@@&..(@@/          @@@*         
                            %@@@@%,,            &@&,&*.             @@*        
                            (@@@@,              @@*(.               .&@,       
                            .&@@@@*               (@,/               &@*       
                             %@@@@@&(,              ,@%/             (&,       
                             %@@&@@@@%*              .@@/           &@%        
                             %@@@@@@@@(,,              @@(%.      %@%%         
                             %@@@@&&@&&%,#              &@&%(#@@@&%          
                            .#@&@@,   ,@@@*/             @@@@@&&&&&            
                            (&@@.        @@@*            &@@@@&@&              
                            %@&.           @@&/          .@@@@*                
                            %@(             @@#*           ,                   
                            %@/             /@@*                               
                            %@/.            #&@&,                              
                             @@*,          /(%@@%*                             
                              %@&(/      /@@@@&@#                              
                                #@@%#@@@@@&@@/               
'''
elakDatorNinja = '''
                     ___..-.---.---.--..___
               _..-- `.`.   `.  `.  `.      --.._
              /    ___________\   \   \______    \\
              |   |.-----------`.  `.  `.---.|   |
              |`. |'  \`.        \   \   \  '|   |
              |`. |'   \ `-._     `.  `.  `.'|   |
             /|   |'    `-._o)\  /(o\   \   \|   |\\
           .' |   |'  `.     .'  '.  `.  `.  `.  | `.
          /  .|   |'    `.  (_.==._)   \   \   \ |.  \         _.--.
        .' .' |   |'      _.-======-._  `.  `.  `. `. `.    _.-_.-' \\
       /  /   |   |'    .'   |_||_|   `.  \   \   \  \  \ .'_.'     ||
      / .'    |`. |'   /_.-'========`-._\  `.  `-._`._`. \(.__      :|
     ( '      |`. |'.______________________.'\      _.) ` )`-._`-._/ /
      \\\      |   '.------------------------.'`-._-'    //     `-._.'
      _\\\_    \    | AMIGA  O O O O * * `.`.|    '     //
     (_  _)    '-._|________________________|_.-'|   _//_
     /  /      /`-._      |`-._     / /      /   |  (_  _)
   .'   \     |`-._ `-._   `-._`-._/ /      /    |    \  \\
  /      `.   |    `-._ `-._   `-._|/      /     |    /   `.
 /  / / /. )  |  `-._  `-._ `-._          /     /   .'      \\
| | | \ \|/   |  `-._`-._  `-._ `-._     /     /.  ( .\ \ \  \\
 \ \ \ \/     |  `-._`-._`-._  `-._ `-._/     /  \  \|/ / | | |
  `.\_\/       `-._  `-._`-._`-._  `-._/|    /|   \   \/ / / /
              /    `-._  `-._`-._`-._  ||   / |    \   \/_/.'
            .'         `-._  `-._`-._  ||  /  |     \\
           /           / . `-._  `-._  || /   |      \\
          '\          / /      `-._    ||/'._.'       \\
           \`.      .' /           `-._|/              \\
            `.`-._.' .'               \               .'
              `-.__\/                 `\            .' '
                                       \`.       _.' .'
                                        `.`-._.-' _.'
                                          `-.__.-'
'''
pvp = '''
       ,               ,
       \              /
        \\0          0/
         |\/      \/|
         |          |
        / \        / \\
   ____/___\______/___\_________ 
'''

#Vi gör en loop som loopar så länge det är sant annars så stänger vi av programet
while loop: 
    runda = 1 
    point1 = 0
    point2 = 0
    if input("Vill du köra?: y/N: ").lower() == "y":
        pc = input("Vem vill du spela mot?: pc/player: ").lower()
        if pc == "pc":
            print(elakDatorNinja)
        else:
            print(pvp)
        while runda < 4:   
        #spelare 1 val av hand
            val1Loop = True
            val2Loop = True
            
            while val1Loop:
                val1 = getpass.getpass("spelare 1 välj din hand: sten, sax, påse: ").lower()
                if val1 == "sten": 
                    val1 = 1
                    val1Loop = False
                elif val1 == "sax":
                    val1 = 2
                    val1Loop = False
                elif val1 == "påse":
                    val1 = 3
                    val1Loop = False
                else:
                    print("Du valde fel. Välj ett av de tre alternativen")
                    val1Loop = True
 
            #spelare 2 val av hand
            if pc == "pc":
                print("Datorn väljer...")
                val2 = random.randint(1,3)
                time.sleep(random.randint(1,5))

            else:
                while val2Loop:
                    val2 = getpass.getpass("Spelare 2 välj din hand: sten, sax, påse: ").lower()
                    if val2 == "sten": 
                        val2 = 1
                        val2Loop = False
                    elif val2 == "sax":
                        val2 = 2
                        val2Loop = False
                    elif val2 == "påse":
                        val2 = 3
                        val2Loop = False
                    else:
                        print("Du valde fel. Välj ett av de tre alternativen")
                        val2Loop = True

            if val1 == val2:
                pass 
                print("Det blev lika")
            elif val1 == 1 and val2 == 2:
                point1 += 1
                print(rock)
                print("poäng till spelare 1")
            elif val1 == 2 and val2 == 3:
                point1 += 1
                print(scissors)
                print("poäng till spelare 1")
            elif val1 == 3 and val2 == 1:
                point1 += 1
                print(paper)
                print("poäng till spelare 1")
            else:
                point2 += 1
                if val2 == 1:
                    print(rock)
                elif val2 == 2:
                    print(scissors)
                else:
                    print(paper)
                print("poäng till spelare 2")
            runda += 1
            print("Nästa runda. Poängen är: " + str(point1) + "-" + str(point2))
    else:
        loop = False
print("Spelet avslutas. Tack för att du spelade.")
time.sleep(2)