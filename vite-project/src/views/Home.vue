<script lang="ts">
export default {

  computed: {
    username() {
      // 我们很快就会看到 `params` 是什么
      return this.$route.params.username
    },
  },
  methods: {

    goToDashboard() {
      let isAuthenticated: boolean = true
      if (isAuthenticated) {
        this.$router.push('/dashboard')
      } else {
        this.$router.push('/login')
      }
    },
  },
}
</script>

<template>
  <div>Home</div>
</template>

<style scoped></style>