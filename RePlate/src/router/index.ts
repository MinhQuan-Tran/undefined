import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import LogInView from "@/views/LogInView.vue";
import SignUpView from "@/views/SignUpView.vue";
import CreatePostView from "@/views/CreatePostView.vue";
import CreateRequestView from "@/views/CreateRequestView.vue";
import ProfileView from "@/views/ProfileView.vue";

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
      path: "/createpost",
      name: "createpost",
      component: CreatePostView
    },
    {
      path: "/createrequest",
      name: "createrequest",
      component: CreateRequestView
    },
    {
      path: "/profile",
      name: "profile",
      component: ProfileView
    },
    {
      path: "/profile/edit",
      name: "profile-edit",
      component: () => import("../views/EditProfileView.vue")
    }
  ]
});

export default router;
