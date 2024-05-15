class resultPage {

    elements = {
        userName: () => cy.get('#_valueusername'),
        titleName: () => cy.get('h1'),
        subtitleElement: () => cy.get('.explanation > p')
    }

    validateURL(URL)
    {
        cy.location().should(loc => {
            expect(loc.pathname).to.equal(URL)
         })
    };

    validateTitle(title) 
    {
        this.elements.titleName().should('include.text',title)
    }

    validateName(name) 
    {
        this.elements.userName().should('include.text',name)
    }

    validateSubtitle(subtitle) 
    {
        this.elements.subtitleElement().should("include.text", subtitle)
    }
}



module.exports = new resultPage();