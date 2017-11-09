# ItemView
## Dependencies
- Tizen 2.4 and Higher for Mobile
- Tizen 3.0 and Higher for Wearable

The `Dali::Toolkit::ItemView` class is a scrollable container that can contain many items. It provides several scrollable layouts, as illustrated in the following figure.

**Figure: ItemView layouts**

| Grid                                     | Spiral                                   | Depth                                    |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| ![captured screen2](./media/grid.png) | ![captured screen2](./media/spiral.png) | ![captured screen2](./media/depth.png) |

You can also create your own custom layout by inheriting from the `Dali::Toolkit::ItemLayout` class.

## Implementing ItemFactory

To create a `Dali::Toolkit::ItemView` instance, you must create your own `ItemFactory` class by deriving from the `Dali::Toolkit::ItemFactory` class and providing its instance to the `ItemView::New()` function. `ItemFactory` is an abstract class having 2 pure virtual member functions to create items and get the number of created items. The following basic example shows how to implement an `ItemFactory` class:

```
class MyFactory : public ItemFactory
{
  public:
    virtual unsigned int GetNumberOfItems()
    {
      // Return the number of items
      return MY_ITEM_COUNT;
    }

    virtual Actor NewItem( unsigned int itemId )
    {
      // Create the actor representing
      // the item based on the itemId
      return ImageView::New( MY_IMAGE_PATHS[itemId] );
    }
};
```

The overridden functions in the derived class are called by the `ItemView` object.

## Creating an ItemView

The following basic example shows how to create a `Dali::Toolkit::ItemView` object:

```
// This sample code is for the HelloWorldExample class
// in Creating a DALi Application
class HelloWorldExample : public ConnectionTracker
{
  // Store a factory as a member variable
  MyFactory mFactory;
};

void HelloWorldExample::Create( Application& application )
{
  // Create an ItemView with the factory
  ItemView itemView = ItemView::New( mFactory );
  itemView.SetParentOrigin( ParentOrigin::CENTER );

  // Create a layout
  ItemLayoutPtr spiralLayout = DefaultItemLayout::New( DefaultItemLayout::SPIRAL );

  // Add the layout to the itemView
  itemView.AddLayout( *spiralLayout );
  // More layouts can be created and added to the itemView

  // Activate the layout
  itemView.ActivateLayout( 0, Vector3( Stage::GetCurrent().GetSize() ), 0 );

  // Add the itemView to the stage
  Stage::GetCurrent().Add( itemView );
}
```