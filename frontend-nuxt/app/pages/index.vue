<template>
  <div class="min-h-screen bg-gray-900">
    <!-- Hero -->
    <section class="py-20">
      <UContainer>
        <div class="mx-auto max-w-4xl text-center space-y-8">
          <!-- Hero Box -->
          <div class="bg-gray-800 border-2 border-primary-400 rounded-2xl p-12 shadow-2xl">
            <div class="space-y-6">
              <!-- Badge -->
              <div class="inline-flex items-center gap-2 px-4 py-2 bg-gray-700 border border-primary-400 rounded-full text-sm text-gray-300">
                <UIcon name="i-heroicons-sparkles-20-solid" class="w-5 h-5 text-primary-400" />
                <span>AI-Powered Journaling</span>
              </div>
              
              <!-- Title -->
              <h1 class="text-5xl font-bold text-white leading-tight">
                Where Did The Day Go?
              </h1>
              
              <!-- Description -->
              <p class="text-xl text-gray-300 leading-relaxed max-w-2xl mx-auto">
                Transform your daily reflections with intelligent AI summaries. Capture your thoughts, track your journey, and discover patterns you never knew existed.
              </p>
              
              <!-- CTA Buttons -->
              <div class="flex items-center justify-center gap-4 pt-4">
                <UButton 
                  color="primary" 
                  size="lg"
                  icon="i-heroicons-rocket-launch" 
                  to="/dashboard"
                  class="px-8 py-3 text-lg"
                >
                  Start Journaling
                </UButton>
                <UButton 
                  variant="ghost" 
                  size="lg"
                  icon="i-heroicons-play" 
                  to="#how-it-works"
                  class="px-8 py-3 text-lg text-gray-300 hover:text-white hover:bg-gray-700"
                >
                  See How It Works
                </UButton>
              </div>
            </div>
          </div>
        </div>
      </UContainer>
    </section>

    <!-- Features -->
    <section class="py-20 bg-gray-800">
      <UContainer>
        <div class="text-center mb-16">
          <h2 class="text-4xl font-semibold text-white mb-4">
            Journaling, reimagined with AI
          </h2>
          <p class="text-xl text-gray-300 max-w-2xl mx-auto">
            Capture your daily experiences and let AI help you understand your journey.
          </p>
        </div>
        
        <div class="grid md:grid-cols-3 gap-8">
          <UCard class="bg-gray-700 border-primary-400">
            <template #header>
              <div class="flex items-center gap-3">
                <UIcon name="i-heroicons-document-text" class="w-6 h-6 text-primary-400" />
                <h3 class="text-xl font-semibold text-white">Daily Entries</h3>
              </div>
            </template>
            <p class="text-gray-300">
              Write freely about your day, thoughts, and experiences. No structure required - just pure, unfiltered reflection.
            </p>
          </UCard>
          
          <UCard class="bg-gray-700 border-primary-400">
            <template #header>
              <div class="flex items-center gap-3">
                <UIcon name="i-heroicons-brain" class="w-6 h-6 text-primary-400" />
                <h3 class="text-xl font-semibold text-white">AI Summaries</h3>
              </div>
            </template>
            <p class="text-gray-300">
              Receive intelligent summaries of your entries, highlighting key themes, emotions, and patterns over time.
            </p>
          </UCard>
          
          <UCard class="bg-gray-700 border-primary-400">
            <template #header>
              <div class="flex items-center gap-3">
                <UIcon name="i-heroicons-chart-bar" class="w-6 h-6 text-primary-400" />
                <h3 class="text-xl font-semibold text-white">Insights & Trends</h3>
              </div>
            </template>
            <p class="text-gray-300">
              Discover recurring patterns, mood trends, and insights about your personal growth journey.
            </p>
          </UCard>
        </div>
      </UContainer>
    </section>

    <!-- How It Works -->
    <section id="how-it-works" class="py-20">
      <UContainer>
        <div class="text-center mb-16">
          <h2 class="text-4xl font-semibold text-white mb-4">
            How WDTG works
          </h2>
          <p class="text-xl text-gray-300 max-w-2xl mx-auto">
            Three simple steps to transform your daily reflections.
          </p>
        </div>
        
        <div class="grid md:grid-cols-3 gap-8">
          <UCard class="bg-gray-800 border-primary-400 text-center">
            <div class="space-y-4">
              <div class="w-16 h-16 bg-primary-600 rounded-full flex items-center justify-center mx-auto">
                <span class="text-2xl font-bold text-white">1</span>
              </div>
              <h3 class="text-xl font-semibold text-white">Write</h3>
              <p class="text-gray-300">
                Take a few minutes each day to write about your experiences, thoughts, or anything that's on your mind.
              </p>
            </div>
          </UCard>
          
          <UCard class="bg-gray-800 border-primary-400 text-center">
            <div class="space-y-4">
              <div class="w-16 h-16 bg-primary-600 rounded-full flex items-center justify-center mx-auto">
                <span class="text-2xl font-bold text-white">2</span>
              </div>
              <h3 class="text-xl font-semibold text-white">AI Analysis</h3>
              <p class="text-gray-300">
                Our AI processes your entries to identify themes, emotions, and patterns, creating meaningful summaries.
              </p>
            </div>
          </UCard>
          
          <UCard class="bg-gray-800 border-primary-400 text-center">
            <div class="space-y-4">
              <div class="w-16 h-16 bg-primary-600 rounded-full flex items-center justify-center mx-auto">
                <span class="text-2xl font-bold text-white">3</span>
              </div>
              <h3 class="text-xl font-semibold text-white">Discover</h3>
              <p class="text-gray-300">
                Gain insights about yourself, track your growth, and understand where your days are truly going.
              </p>
            </div>
          </UCard>
        </div>
      </UContainer>
    </section>

    <!-- Benefits -->
    <section class="py-20 bg-gray-800">
      <UContainer>
        <div class="text-center mb-16">
          <h2 class="text-4xl font-semibold text-white mb-4">
            Why choose WDTG?
          </h2>
          <p class="text-xl text-gray-300 max-w-2xl mx-auto">
            More than just a journal - it's your personal growth companion.
          </p>
        </div>
        
        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          <UCard class="bg-gray-700 border-primary-400 text-center">
            <div class="space-y-3">
              <UIcon name="i-heroicons-eye" class="w-8 h-8 text-primary-400 mx-auto" />
              <h3 class="text-lg font-semibold text-white">Self-Awareness</h3>
              <p class="text-sm text-gray-300">
                Gain deeper insights into your thoughts, emotions, and behaviors through AI-powered pattern recognition.
              </p>
            </div>
          </UCard>
          
          <UCard class="bg-gray-700 border-primary-400 text-center">
            <div class="space-y-3">
              <UIcon name="i-heroicons-clock" class="w-8 h-8 text-primary-400 mx-auto" />
              <h3 class="text-lg font-semibold text-white">Time Well Spent</h3>
              <p class="text-sm text-gray-300">
                Make your daily reflections more meaningful with intelligent summaries that save you time while providing value.
              </p>
            </div>
          </UCard>
          
          <UCard class="bg-gray-700 border-primary-400 text-center">
            <div class="space-y-3">
              <UIcon name="i-heroicons-heart" class="w-8 h-8 text-primary-400 mx-auto" />
              <h3 class="text-lg font-semibold text-white">Emotional Intelligence</h3>
              <p class="text-sm text-gray-300">
                Track your emotional patterns and develop better understanding of your mental health and well-being.
              </p>
            </div>
          </UCard>
          
          <UCard class="bg-gray-700 border-primary-400 text-center">
            <div class="space-y-3">
              <UIcon name="i-heroicons-arrow-trending-up" class="w-8 h-8 text-primary-400 mx-auto" />
              <h3 class="text-lg font-semibold text-white">Personal Growth</h3>
              <p class="text-sm text-gray-300">
                Identify areas for improvement and celebrate your progress with data-driven insights about your journey.
              </p>
            </div>
          </UCard>
        </div>
      </UContainer>
    </section>

    <!-- CTA -->
    <section class="py-20">
      <UContainer>
        <div class="text-center">
          <UCard class="bg-gray-800 border-primary-400 max-w-3xl mx-auto">
            <div class="space-y-6">
              <h3 class="text-3xl font-semibold text-white">
                Ready to discover where your days are going?
              </h3>
              <p class="text-xl text-gray-300">
                Start your AI-powered journaling journey today and gain insights you never knew existed.
              </p>
              <!-- <div class="flex items-center justify-center gap-4 pt-4">
                <UButton 
                  color="primary" 
                  size="lg"
                  icon="i-heroicons-rocket-launch" 
                  to="/dashboard"
                  class="px-8 py-3 text-lg"
                >
                  Start Journaling
                </UButton>
                <UButton 
                  variant="ghost" 
                  size="lg"
                  icon="i-heroicons-information-circle" 
                  to="/about"
                  class="px-8 py-3 text-lg text-gray-300 hover:text-white hover:bg-gray-700"
                >
                  Learn More
                </UButton>
              </div> -->
            </div>
          </UCard>
        </div>
      </UContainer>
    </section>
  </div>
</template>

<script setup lang="ts">
useSeoMeta({
  title: 'WDTG - Where Did The Day Go | AI-Powered Journaling',
  ogTitle: 'WDTG - Where Did The Day Go | AI-Powered Journaling',
  description: 'Transform your daily reflections with intelligent AI summaries. Capture your thoughts, track your journey, and discover patterns you never knew existed.',
  ogDescription: 'Transform your daily reflections with intelligent AI summaries. Capture your thoughts, track your journey, and discover patterns you never knew existed.',
})
</script>



