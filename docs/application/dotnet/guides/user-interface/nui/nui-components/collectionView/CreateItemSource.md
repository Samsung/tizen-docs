---
keyword: CollectionView, RecyclerView, listview, gridview, itemsview, ObservableCollection, List, ItemSource, INotifyPropertyChanged, groupableView
---

## Create item source

To use [`CollectionView`](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Components.CollectionView.html), item source need to be created firstly. Item source is the collection of data on each item, which can notify the changes on demands.

1. Create an model class of item data:
    ```csharp
    class Animal
    {
        private string _name;
        private string _scientificName;
        private string _imageResource;
        private string _imageUrl = Tizen.Applications.Application.Current.DirectoryInfo.Resource + "/animals/";

        public Animal(string name, string scientificName, string imageResource)
        {
            _name = name;
            _scientificName = scientificName;
            _imageResource = imageResource;
        }

        public string Name
        {
            get => _name;
            set => _name = value;
        }

        public string ScientificName
        {
            get => _scientificName;
            set => _scientificName = value;
        }

        public string ImagePath
        {
            get => _imageUrl + _imageResource;
        }
    }
    ```
    To apply properties changes dynamically in the CollectionView, you need to implement [`System.ComponentModel.INotifyPropertyChanged`](https://learn.microsoft.com/En-us/dotnet/api/system.componentmodel.inotifypropertychanged?view=netstandard-2.0) interface.

    ```csharp
    class Animal : INotifyPropertyChanged
    {
        public event PropertyChangedEventHandler PropertyChanged;

        public string Name
        {
            get => _name;
            set
            {
                _name = value;
                //Invoke property changed event when property changed.
                PropertyChanged?.Invoke(this, new PropertyChangedEventArgs("Name"));
            }
        }
    }
    ```

2. Create [`System.Collections.Generic.IEnumerable`](https://learn.microsoft.com/en-us/dotnet/api/system.collections.ienumerable?view=netstandard-2.0) data collection for items. for simple collection, [`System.Collections.Generic.List<T>`](https://learn.microsoft.com/En-us/dotnet/api/system.collections.generic.list-1?view=netstandard-2.0) can be useful:

    ```csharp
    var animals = new List<Animal>();
    animals.Add(new Animal("Cat", "Felis catus", "cat.png"));
    animals.Add(new Animal("Dog", "Canis lupus familiaris", "dog.png"));
    animals.Add(new Animal("Fox", "Vulpes" "fox.png"));
    animals.Add(new Animal("Horse", "Equus ferus", "horse.png"));
    ```

    To apply data changes dynamically in the CollectionView, you need to implement [`System.ComponentModel.INotifyPropertyChanged`](https://learn.microsoft.com/En-us/dotnet/api/system.componentmodel.inotifypropertychanged?view=netstandard-2.0) and [`System.Collections.Specialized.INotifyCollectionChanged`](https://learn.microsoft.com/en-us/dotnet/api/system.collections.specialized.inotifycollectionchanged?view=netstandard-2.0) interface.
   [`System.Collections.ObjectModel.ObservableCollection<T>`](https://learn.microsoft.com/en-us/dotnet/api/system.collections.objectmodel.observablecollection-1?view=netstandard-2.0) can be useful for this purpose.

    ```csharp
    var animals = new ObservableCollection<Animal>();
    ```

## Create grouped item source

CollectionView support grouped item source with  [`System.Collections.ObjectModel.ObservableCollection<T>`](https://learn.microsoft.com/en-us/dotnet/api/system.collections.objectmodel.observablecollection-1?view=netstandard-2.0):
1. Create   [`System.Collections.ObjectModel.ObservableCollection<T>`](https://learn.microsoft.com/en-us/dotnet/api/system.collections.objectmodel.observablecollection-1?view=netstandard-2.0) data collection for group:

    ```csharp
    class Family : ObservableCollection<Animal>
    {
        private string _name;
        public Family(string name)
        {
            _name = name;
        }

        public Name
        {
            get => _name;
            set
            {
                _name = value;
                OnPropertyChanged(new PropertyChangedEventArgs("Name"));
            }
        }
    }
   ```
2. add group into group collection:

    ```csharp

    var families = new ObservableCollection<Family>();

    var falidae = new Family("Falidae");
    falidae.Add(new Animal("Cat", "Felis catus", "cat.png"));
    falidae.Add(new Animal("Cheetah", "Acinonyx jubatus", "cheetah.png"));
    falidae.Add(new Animal("Leopard", "Panthera pardus", "leopard.png"));
    falidae.Add(new Animal("Lion", "Panthera leo", "lion.png"));
    falidae.Add(new Animal("Tiger", "Panthera tigris", "tiger.png"));
    families.Add(falidae);

    var canidae = new Family("Canidae");
    canidae.Add(new Animal("Coyote", "Canis latrans" "coyote.png"));
    canidae.Add(new Animal("Dog", "Canis lupus familiaris", "dog.png"));
    canidae.Add(new Animal("Fox", "Vulpes" "fox.png"));
    canidae.Add(new Animal("Raccoon dog", "Nyctereutes procyonoides" "raccoondog.png"));
    canidae.Add(new Animal("Wolf", "Canis lupus" "wolf.png"));
    families.Add(canidae);
    ```


## Related information

- Dependencies
  -   Tizen 7.0 and Higher
