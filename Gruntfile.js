module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    uglify: {
      options: {
        banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n'
      },
      build: {
        src: 'static/js/<%= pkg.name %>.js',
        dest: 'static/js/<%= pkg.name %>.min.js'
      }
    },

    less: {
      options: {
        compress: true,
        yuicompress: true,
        optimization: 2
      },
      files: {
        "static/css/main.css": "assets/private/css/source.less"
      }
    }

    watch: {
      styles: {
        // Which files to watch (all .less files recursively in the less directory)
        files: ['sites/all/themes/jiandan/less/**/*.less'],
        tasks: ['less'],
        options: {
          nospawn: true
        }
      }
    }
    watch: {
      css: {
        files: [
          '**/*.sass',
          '**/*.scss'
        ],
        tasks: ['compass']
      },
      js: {
        files: [
          'static/js/*.js',
          'Gruntfile.js'
        ],
        tasks: ['jshint']
      }
    }
  });

  // Load the plugin that provides the "uglify" task.
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-less');

  // Default task(s).
  grunt.registerTask('default', ['uglify', 'watch']);

};

