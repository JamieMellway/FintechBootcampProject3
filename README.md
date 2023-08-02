# FintechBootcampProject3
Project 3 for Fintech Bootcamp 

## Buying and Selling Property
This app allows a user to list and buy properties.

### How it works
A user will list their property for sale. The information associated with the property is stored on [Piñata](https://www.pinata.cloud/), including images. An [OpenZeppelin ERC721](https://docs.openzeppelin.com/contracts/2.x/erc721) token is created for the property. All contracts are coded with [Solidity](https://soliditylang.org/) in [Remix](https://remix.ethereum.org/).

The token contract inherits ERC721 as well as a custom contract for transfering Ether from buyer to seller through the contract.

#### Selling/Listing    
1. Click on the 'List Property' option from the drop-down in the sidebar.
2. Fill in all the information including adding pictures of your property.
3. Click 'List!'

#### Buying    
1. Click on the 'Buy Property' option from the drop-down in the sidebar.
2. Fill in all the information.
3. Click on 'Buy'

