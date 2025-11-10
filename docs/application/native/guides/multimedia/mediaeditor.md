# Media Editor


The Media Editor API allows you to edit media clips and create output media files in your applications.

The main features of the Media Editor API include:

- [Timeline management](#timeline)

  You can create and manage a timeline composed of layers and clips. Layers determine the hierarchical ordering of clips, and you can add, remove, and rearrange both layers and clips.

- [Clip operations](#clip_operations)

  You can add, remove, split, group, and ungroup media clips. You can also modify clip properties such as start time, duration, position, resolution, and volume.

- [Layer management](#layer_management)

  You can add, remove, and move layers. You can also activate or deactivate layers to include or exclude them from rendering.

- [Effects and transitions](#effects)

  You can add video and audio effects to clips, as well as transition effects between overlapping clips.

- [Preview and rendering](#preview_render)

  You can preview your edits in real-time or render the final output to a file.

- [Project management](#project)

  You can save and load editing projects to preserve your work and continue editing later.

## Prerequisites

To enable your application to use the mediaeditor functionality:

1. To use the functions and data types of the Media Editor API, include the `<media_editor.h>` header file in your application:

   ```
   #include <media_editor.h>
   ```

2. Create a media editor handle using `mediaeditor_create()`:

   ```
   mediaeditor_h editor = NULL;
   int error_code = mediaeditor_create(&editor);
   if (error_code != MEDIAEDITOR_ERROR_NONE) {
       // Handle error
   }
   ```

<a name="timeline"></a>
## Managing the timeline

The timeline is the core component of the media editor, composed of layers that contain clips. The timeline allows you to arrange and edit your media content.

To work with the timeline:

1. Create a media editor handle as shown in the prerequisites.

2. Add layers to the timeline using `mediaeditor_add_layer()`:

   ```
   unsigned int layer_id, layer_priority;
   int error_code = mediaeditor_add_layer(editor, &layer_id, &layer_priority);
   if (error_code != MEDIAEDITOR_ERROR_NONE) {
       // Handle error
   }
   ```

3. Add clips to layers using `mediaeditor_add_clip()`:

   ```
   unsigned int clip_id;
   // Add a clip to the beginning of the layer
   int error_code = mediaeditor_add_clip(editor, "/path/to/media/file.mp4", layer_id, 
                                        0, 5000, 0, &clip_id);
   if (error_code != MEDIAEDITOR_ERROR_NONE) {
       // Handle error
   }
   ```

<a name="clip_operations"></a>
## Performing clip operations

You can perform various operations on clips to edit your media content.

### Splitting clips

To split a clip at a specific position:

```
unsigned int new_clip_id;
int error_code = mediaeditor_split_clip(editor, clip_id, 3000, &new_clip_id);
if (error_code != MEDIAEDITOR_ERROR_NONE) {
    // Handle error
}
```

### Grouping and ungrouping clips

To group multiple clips together:

```
unsigned int clip_ids[2] = {clip_id1, clip_id2};
unsigned int group_id;
int error_code = mediaeditor_group_clip(editor, clip_ids, 2, &group_id);
if (error_code != MEDIAEDITOR_ERROR_NONE) {
    // Handle error
}
```

To ungroup clips:

```
unsigned int *ungrouped_clip_ids;
unsigned int size;
int error_code = mediaeditor_ungroup_clip(editor, group_id, &ungrouped_clip_ids, &size);
if (error_code != MEDIAEDITOR_ERROR_NONE) {
    // Handle error
}
// Don't forget to free the ungrouped_clip_ids array
free(ungrouped_clip_ids);
```

### Modifying clip properties

To modify clip properties such as start time, duration, position, resolution, and volume:

```
// Set clip start time
int error_code = mediaeditor_set_clip_start(editor, clip_id, 1000);
if (error_code != MEDIAEDITOR_ERROR_NONE) {
    // Handle error
}

// Set clip duration
error_code = mediaeditor_set_clip_duration(editor, clip_id, 4000);
if (error_code != MEDIAEDITOR_ERROR_NONE) {
    // Handle error
}

// Set clip position
error_code = mediaeditor_set_clip_position(editor, clip_id, 100, 50);
if (error_code != MEDIAEDITOR_ERROR_NONE) {
    // Handle error
}

// Set clip resolution
error_code = mediaeditor_set_clip_resolution(editor, clip_id, 1920, 1080);
if (error_code != MEDIAEDITOR_ERROR_NONE) {
    // Handle error
}

// Set clip volume
error_code = mediaeditor_set_clip_volume(editor, clip_id, 1.5);
if (error_code != MEDIAEDITOR_ERROR_NONE) {
    // Handle error
}
```

<a name="layer_management"></a>
## Managing layers

You can manage layers to organize your clips hierarchically.

### Moving layers

To move a layer to a different priority position:

```
int error_code = mediaeditor_move_layer(editor, layer_id, new_priority);
if (error_code != MEDIAEDITOR_ERROR_NONE) {
    // Handle error
}
```

### Activating and deactivating layers

To activate or deactivate layers:

```
// Activate a layer
int error_code = mediaeditor_activate_layer(editor, layer_id);
if (error_code != MEDIAEDITOR_ERROR_NONE) {
    // Handle error
}

// Deactivate a layer
error_code = mediaeditor_deactivate_layer(editor, layer_id);
if (error_code != MEDIAEDITOR_ERROR_NONE) {
    // Handle error
}
```

<a name="effects"></a>
## Adding effects and transitions

You can enhance your media content by adding effects and transitions.

### Adding video and audio effects

To add effects to clips:

```
unsigned int effect_id;
int error_code = mediaeditor_add_effect(editor, MEDIAEDITOR_EFFECT_VIDEO_TYPE_AGINGTV, 
                                       layer_id, 0, 5000, &effect_id);
if (error_code != MEDIAEDITOR_ERROR_NONE) {
    // Handle error
}
```

### Adding transitions

To add transitions between overlapping clips:

```
int error_code = mediaeditor_add_transition(editor, MEDIAEDITOR_TRANSITION_TYPE_CROSSFADE, 
                                           layer_id, 4000, 1000);
if (error_code != MEDIAEDITOR_ERROR_NONE) {
    // Handle error
}
```

<a name="preview_render"></a>
## Previewing and rendering

You can preview your edits in real-time or render the final output to a file.

### Previewing

To preview your edits:

```
// Set display for preview
int error_code = mediaeditor_set_display(editor, MEDIAEDITOR_DISPLAY_TYPE_EVAS, display_handle);
if (error_code != MEDIAEDITOR_ERROR_NONE) {
    // Handle error
}

// Start preview
error_code = mediaeditor_start_preview(editor);
if (error_code != MEDIAEDITOR_ERROR_NONE) {
    // Handle error
}

// Stop preview
error_code = mediaeditor_stop_preview(editor);
if (error_code != MEDIAEDITOR_ERROR_NONE) {
    // Handle error
}
```

### Rendering

To render the final output:

```
// Define callback for render completion
void render_completed_cb(void *user_data) {
    // Handle render completion
}

// Start rendering
int error_code = mediaeditor_start_render(editor, "/path/to/output/file.mp4", 
                                         render_completed_cb, NULL);
if (error_code != MEDIAEDITOR_ERROR_NONE) {
    // Handle error
}
```

<a name="project"></a>
## Managing projects

You can save and load editing projects to preserve your work.

### Creating and saving projects

To create and save a project:

```
// Create a new project
int error_code = mediaeditor_create_project(editor, "/path/to/project/file.mep");
if (error_code != MEDIAEDITOR_ERROR_NONE) {
    // Handle error
}

// Save the current project
error_code = mediaeditor_save_project(editor);
if (error_code != MEDIAEDITOR_ERROR_NONE) {
    // Handle error
}
```

### Loading projects

To load an existing project:

```
// Define callback for project loading
void project_loaded_cb(void *user_data) {
    // Handle project loaded
}

// Load a project
int error_code = mediaeditor_load_project(editor, "/path/to/project/file.mep", 
                                         project_loaded_cb, NULL);
if (error_code != MEDIAEDITOR_ERROR_NONE) {
    // Handle error
}
```

## Related information
- Dependencies
  - Since Tizen 7.0
- API references
  - [Media Editor](../../api/common/latest/group__CAPI__MEDIA__EDITOR__MODULE.html)
