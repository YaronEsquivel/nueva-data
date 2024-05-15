Feature: Form Page
  
  @ScenarioSimple
  Scenario: The user is the page
    Given A web browser is at the demoqa page
    When The user is select form
    And A user enters the firstname "Axity"
    And A user enters the lastname "Desarrollo de Aplicaciones"
    And The user enters his current address "Av.Palams"
    And The user select picture ".//cypress//e2e//resources//descarga.png"
    And The user select his hobbies "Checkbox 1, Checkbox 2 and Checkbox 3"
    And The user select his gender "radio 3"
    And A user select multiple items "Selection Item 1andSelection Item 2"
    And A user select dropdown "Drop Down Item 5"
    And A user confirm form 
    Then the system navigates to result page "/styled/the_form_processor.php"
    And the page shows the title "Processed Form Details"
    And the page shows the subTitle 
    And the page shows the captured name "Axity"


  @ScenarioTable
  Scenario Outline: The user is the page
    Given A web browser is at the demoqa page
    When The user is select form
    And A user enters the firstname "<firstname>"
    And A user enters the lastname "<lastname>"
    And The user enters his current address "<currentAddress>"
    And The user select picture "<picture>"
    And The user select his hobbies "<hobbies>"
    And The user select his gender "<gender>"
    And A user select multiple items "<items>"
    And A user select dropdown "<dropdown>"
    And A user confirm form
    Then the system navigates to result page "/styled/the_form_processor.php"
    And the page shows the title "Processed Form Details"
    And the page shows the subTitle 
    And the page shows the captured name "<firstname>"
    Examples:
      | firstname | lastname | currentAddress               | picture                                        | hobbies                               | gender  | items                               | dropdown         |
      | Karina      | Reyes    | Calle Las begonias SJm       | ./cypress/e2e/resources/descarga.png | Checkbox 1, Checkbox 2 and Checkbox 3 | radio 3 | Selection Item 1andSelection Item 2 | Drop Down Item 5 |
      | Osvaldo   | Zamora    | San Martin de Porres 120 SMP | ./cypress/e2e/resources/descarga.png | Checkbox 1 and Checkbox 2             | radio 1 | Selection Item 2andSelection Item 3 | Drop Down Item 5 |