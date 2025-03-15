<template>
  <div class="about">
    <h2 class="title">Our Purpose</h2>
    <p class="powerful_description">Turning food waste into community support: RePlate.</p>
    <b></b>
    <p class="description">
      RePlate aims to eliminate food waste and foster community values by bridging the gap between businesses with surplus food and individuals and charities who can use it. </p>
    <p class="description">Whether we are connecting bakeries with unsold pastries or a restuarant with extra meals, we make it easy for them to connect with local organisations and people in real time. Businesses reduce waste, and people in need are able to access sustainable, quality meals. 
    </p>
    <h2 class="title">What We Do</h2>
    <p class="description">We connect people and businesses with excess food, with those who need it. If you have perfectly good food that will otherwise go to waste, simply post a photo of the food and what people need to know, and others can come and collect it!</p>
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
  .title {
    color: forestgreen;
    font-size: 2rem;
    margin-bottom: 20px;
  }
  .description {
    font-size: 1rem;
    max-width: 800px;
    line-height: 1.5;
  }
  .powerful_description {
    font-size: 1.25rem;
    max-width: 800px;
    color:forestgreen;
    line-height: 1.5;
  }
}
</style>
