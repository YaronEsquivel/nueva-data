import { Given, When, Then } from "@badeball/cypress-cucumber-preprocessor";


const resultPage =require("../../pages/resultPage")

Then ("the system navigates to result page {string}" ,(url) =>
{
    resultPage.validateURL(url);
})

Then ("the page shows the title {string}" ,(title) => 
{
    resultPage.validateTitle(title)
})

Then ("the page shows the subTitle",() => 
{
    resultPage.validateSubtitle("You submitted a form. The details below show the values you entered for processing.")
})


Then ("the page shows the captured name {string}",(name) => 
{
    resultPage.validateName(name)
    cy.screenshot('resultform-evidence1');
})
