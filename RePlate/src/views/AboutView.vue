<template>
  <div class="about"style="overflow: scroll; max-width: fit-content; max-height: fit-content;">
    <h1 class="main_title">RePlate</h1>
    <h2 class="title">
      <p>Our Purpose </p>
      <img alt="Our Purpose" src="@/assets/our-purpose.png" width="50" height="50" />
    </h2>
    
    <p class="powerful_description" style="font-size: 1.25rem; max-width: 800px;color: forestgreen;line-height: 1.5px;">Turning food waste into community support: RePlate.</p>
    <br></br>
    <p></p>
    <p class="description">
      RePlate aims to eliminate food waste and foster community values by bridging the gap between businesses with surplus food and individuals and charities who can use it. </p>
    <p class="description">Whether we are connecting bakeries with unsold pastries or a restuarant with extra meals, we make it easy for them to connect with local organisations and people in real time. Businesses reduce waste, and people in need are able to access sustainable, quality meals. 
    </p>
    <h2 class="title">
      <p>What We Do </p>
      <img alt="What we do" src="@/assets/what-we-do.png" width="50" height="50" />
    </h2>
    <p class="description">We connect people and businesses with excess food, with those who need it. If you have perfectly good food that will otherwise go to waste, simply post a photo of the food and what people need to know, and others can come and collect it!</p>
    <h2 class="title">
      <p>Who are we?</p>
      <img alt="Us" src="@/assets/the-team.png" width="50" height="50" />

    </h2>
    <p class="description"> We are a group of University students who are passionate about sustainability and supporting our local community. Being the change we want to see: we have embarked on this journey to minimise quality food that goes to the bin, hoping that one day no one has to go to bed hungry.</p>
    <h2 class="title">
      <p>Get involved</p>
      <img alt="Unity Image" src="@/assets/unity.png" width="50" height="50" />
    </h2>
    <p class="description">No matter how big or small: Sign up today to start sharing and collecting valuable ingredients.</p>
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
  }
  .main_title {
    color: rgb(31, 126, 31);
    font-size: 3rem;
    font-weight: 600;
    margin-bottom: 20px;
    display: flex;

  }
  .title {
    color: forestgreen;
    font-size: 2rem;
    margin-bottom: 20px;
    display: flex;
    flex-direction: 'row'
  }
  .description {
    font-size: 1rem;
    max-width: 800px;
    line-height: 1.5;
    color: black;
  }
}
</style>

