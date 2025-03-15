import { createRouter, createWebHistory } from "vue-router";
// import HomeView from "../views/HomeView.vue";
import LogInView from "@/views/LogInView.vue";
import SignUpView from "@/views/SignUpView.vue";
import FeedView from "@/views/FeedView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/login",
      name: "login",
      component: LogInView
      // path: "/",
      // name: "home",
      // component: HomeView
    },
    {
      path: "/",
      name: "about",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/AboutView.vue")
    },
    {
      path: "/template",
      name: "template",
      component: () => import("../views/TemplateView.vue")
    },
    {
      path: "/signup",
      name: "signup",
      component: SignUpView
    },
    {
      path: "/feed",
      name: "feed",
      component: FeedView
    },
  ]
});

export default router;
