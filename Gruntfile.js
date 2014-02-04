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
        "static/css/main.css": "static/less/main.less"
      }
    },
    coffee: {
      files: {
        'static/js/main.js': 'static/coffee/main.coffee', // 1:1 compile
      }
    },

    watch: {
      styles: {
        options: {
          spawn: false
        },
        files: [ "static/css/main.css", "static/less/main.less"],
        tasks: [ "less" ]
      },
      coffee: {
        files: ['static/coffee/main.coffee'],
        tasks: ['coffee']
      }
    }

  });

  // Load the plugin that provides the "uglify" task.
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-contrib-coffee');

  // Default task(s).
  grunt.registerTask('default', ['less', 'coffee', 'watch']);

};

