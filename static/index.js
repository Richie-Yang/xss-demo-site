const tooltipTextList = document.getElementsByClassName('tooltiptext');
try {
    for (let i = 0; i < tooltipTextList.length; i++) {
        if (tooltipTextList[i].id === 'reflected') {
            tooltipTextList[i].innerText = "Reflected XSS or Non-persistent XSS is a type of XSS. In this type, the " +
                "attacker’s payload becomes a part of the request that goes to the webserver. Then, it is reflected " +
                "back in a way that the HTTP response includes the payload from the HTTP request. The attacker can use " +
                "malicious links, phishing email, etc. to make the users send requests to the server. Finally, " +
                "the reflected XSS payload is executed in the user’s browser. As reflected XSS is not a persistent " +
                "attack, the attacker has to deliver the payload to each victim."
        } else if (tooltipTextList[i].id === 'storeBased') {
            tooltipTextList[i].innerText = "Out of the three types of XSS, attackers are most interested by stored XSS. " +
                "The reason for that is that the reach of the malicious code through stored XSS is enormous. It takes " +
                "fewer resources to target a larger number of victims. And once the malicious code is in place, its " +
                "effect is continuous. If stored XSS isn’t identified and mitigated, the malicious code will " +
                "keep doing its job for a ton of users and can go on for decades."
        } else if (tooltipTextList[i].id === 'domBased') {
            tooltipTextList[i].innerText = "DOM-based XSS is an advanced XSS attack. Here, the web application reads " +
                "the data from the DOM and output them to the browser. Moreover, if in the case of incorrect handling " +
                "of data, the attacker can inject a payload to store as a part of DOM."
        }
    }
} catch (error) {}




